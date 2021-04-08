#include "mypreimageshow.h"
#include "ui_mypreimageshow.h"
#include "prescorepage.h"
#include "ui_prescorepage.h"
#include <fstream>
#include <QDir>
#include <random>
#include <ctime>
#include <algorithm>
#include <QDebug>
#include <io.h>
#include <QPixmap>
#include <QMessageBox>
#include <QImage>
#include <QKeyEvent>
#include <QTimer>
#include <QTime>
myPreImageShow::myPreImageShow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::myPreImageShow),timer(new QTimer),__ScorePage(new PreScorePage)
{
    ui->setupUi(this);
    setFocusPolicy(Qt::StrongFocus);
    setWindowState(Qt::WindowMaximized);
    setWindowFlag(Qt::FramelessWindowHint);
    currentNum = 1;
    currentImagePart =0;
    Testnumber = "测试专用";
    timer->stop();
    timer->setInterval(500);
    IsTestTime =true;
    IsEnterEnable = false;
    DataDir = "./database";
    scantimeAll = 60;
    scantimePart = 60;
    scantimeRestAll = 8;
    scantimeRestPart = 3;
    IsRight = true;
    restime = scantimeAll;
    iniSignalSlots();
    __IfScorePage = false;
    QVector<QPixmap> img_set;
    partNum = 5;
}
void myPreImageShow::receive_info(QString num,QString path)
{
    Testnumber = num;
    DataDir = path;
    showFullScreen();
    QMessageBox::information(this, "预热试验提示框", "您将首先进入一段预热实验，其目的在于帮助您更好的熟悉实验的流程。你只需要根据提示进行操作即可");
    get_image_info();
    one_image_test_get();
    one_image_score();
}

void myPreImageShow::iniSignalSlots()
{   
    connect(timer,SIGNAL(timeout()),this,SLOT(do_timer_timeout()));
    connect(__ScorePage,SIGNAL(score_signal()),this,SLOT(OneImageFinish()));
}

void myPreImageShow::get_image_info()
{
    srand(time(NULL));
    image_dir = DataDir+"/PreImg/images";
    label_dir = DataDir+"/PreImg/labels";
    QDir Imagedir(image_dir);
    QDir Labeldir(label_dir);
    //设置文件过滤器
    QStringList nameFilters;
    //设置文件过滤格式
    nameFilters << "*.bmp";
    //将过滤后的文件名称存入到files列表中
    imageList = Imagedir.entryList(nameFilters, QDir::Files|QDir::Readable, QDir::Name);
    labelList = Labeldir.entryList(nameFilters, QDir::Files|QDir::Readable, QDir::Name);
    testNum = imageList.size();
}
void myPreImageShow::one_image_test_get()
{
    QString imagePath = image_dir+"/"+imageList[currentNum-1];
    QString labelPath = label_dir+"/"+imageList[currentNum-1];
    while(!img_set.empty())
    {
        img_set.pop_back();
    }
    QImage image(imagePath.toUtf8().data());
    QImage label(labelPath.toUtf8().data());
    int label_y = label.height();
    int label_x = label.width();
    img_set.push_back(image);
    QSet<double> label_set;
    for(int i=0;i<label_x;i++)
    {
       for(int j=0;j<label_y;j++)
       {
           label_set.insert(label.pixelColor(i,j).red());
       }
    }
    partNum = label_set.size();
    QColor oldColor;
    for(int k=0;k<partNum;k++)
    {
        QImage newImage = image;
        for(int i=0;i<label_x;i++)
        {
           for(int j=0;j<label_y;j++)
           {
               if(label.pixelColor(i,j).red()!= k+1)
               {
                   QRgb rgb = image.pixel(i,j);
                   int r = qRed(rgb)*0.15;
                   int g = qGreen(rgb)*0.15;
                   int b = qBlue(rgb)*0.15;
                   newImage.setPixel(i,j,qRgb(r,g,b));
               }
           }
        }
        img_set.push_back(newImage);
    }
    switch(currentNum)
    {
    case 1:
          QMessageBox::information(this, "预热试验提示框", "接下来你会看到一张图片，该图片是一张质量很好的图片，我们倾向于给这张图片较高的分数");
          break;
    case 2:
          QMessageBox::information(this, "预热试验提示框", "接下来你会看到一张图片，该图片是一张质量一般的图片，我们倾向于给这张图片中等的分数");
          break;
    case 3:
          QMessageBox::information(this, "预热试验提示框", "接下来你会看到一张图片，该图片是一张质量很差的图片，我们倾向于给这张图片较低的分数");
          break;
    default:
          break;
    }
}
void myPreImageShow::one_image_score()
{
    if(IsRight)
    {
        ui->imageShow->setStyleSheet("background-color:#808080");
        QImage curPixmap = img_set[currentImagePart];
        QPixmap p;
        ui->imageShow->setPixmap(p.fromImage(curPixmap));
        if(currentImagePart == 0)
        {
            restime = scantimeAll;
        }
        else
        {
            restime = scantimePart;
        }
        timer->start();
    }

}
void myPreImageShow::do_timer_timeout()
{
    restime = restime - 1;
    if(currentImagePart == 0)
    {
       if(restime <= scantimeAll - scantimeRestAll)
           IsEnterEnable = true;
       else
           IsEnterEnable = false;
    }
    else
    {
       if(restime <= scantimePart - scantimeRestPart)
            IsEnterEnable = true;
       else
            IsEnterEnable = false;
    }
    if(restime == 0)
    {
       timer->stop();
       __ScorePage->show();
       QPixmap curPixmap = QPixmap();
       ui->imageShow->setStyleSheet("background-color:#808080");
       ui->imageShow->setPixmap(curPixmap);
       __ScorePage->ui->finishedEdit->setText(QString::number(currentNum)+"/"+QString::number(testNum));
       if(currentNum == 1 && currentImagePart == 0)
       {
           __ScorePage->ui->plainTextEdit->clear();
           __ScorePage->ui->plainTextEdit->appendPlainText("可以看出，刚才显示的照片的质量很不错");
           __ScorePage->ui->plainTextEdit->appendPlainText("因此您可以去拖动左边的滑块，选择一个较高的分数");
           __ScorePage->ui->plainTextEdit->appendPlainText("例如：");
           __ScorePage->ui->lineEdit->setText("85分");
       }
       else if(currentNum == 2 && currentImagePart == 0)
       {
           __ScorePage->ui->plainTextEdit->clear();
           __ScorePage->ui->plainTextEdit->appendPlainText("可以看出，刚才显示的照片的质量一般");
           __ScorePage->ui->plainTextEdit->appendPlainText("因此您可以去拖动左边的滑块，选择一个中等的分数");
           __ScorePage->ui->plainTextEdit->appendPlainText("例如：");
           __ScorePage->ui->lineEdit->setText("50分");
       }
       else if(currentNum == 3 && currentImagePart == 0)
       {
           __ScorePage->ui->plainTextEdit->clear();
           __ScorePage->ui->plainTextEdit->appendPlainText("可以看出，刚才显示的照片的质量很差");
           __ScorePage->ui->plainTextEdit->appendPlainText("因此您可以去拖动左边的滑块，选择一个较低的分数");
           __ScorePage->ui->plainTextEdit->appendPlainText("例如：");
           __ScorePage->ui->lineEdit->setText("15分");
       }
       else
       {
           __ScorePage->ui->plainTextEdit->clear();
           __ScorePage->ui->plainTextEdit->appendPlainText("你可以根据你的观察给予合适的局部评分");
           __ScorePage->ui->lineEdit->setText("");
       }
       if(currentImagePart ==0)
            __ScorePage->ui->currentPartEdit->setText("整体");
       else
            __ScorePage->ui->currentPartEdit->setText("局部" + QString::number(currentImagePart));
    }

}

void myPreImageShow::OneImageFinish()
{
    IsEnterEnable = false;
    if(currentImagePart == partNum)
    {
        currentImagePart = 0;
        if(currentNum == testNum)
        {
           __ScorePage->close();
           QMessageBox::information(this,"预实验结束信息框","预热实验已经结束，下面将进行正式实验");
           emit endpre(Testnumber,DataDir);
           close();
        }
        else
        {
            currentNum = currentNum + 1;
            one_image_test_get();
            one_image_score();
        }
    }
    else
    {
        currentImagePart=currentImagePart + 1;
        one_image_score();
    }
}
void myPreImageShow::keyPressEvent(QKeyEvent *event)
{
    if(event->key() == Qt::Key_Return && IsEnterEnable == true)
    {
        timer->stop();
        __ScorePage->show();
        QPixmap curPixmap = QPixmap();
        ui->imageShow->setStyleSheet("background-color:#808080");
        ui->imageShow->setPixmap(curPixmap);
        __ScorePage->ui->finishedEdit->setText(QString::number(currentNum)+"/"+QString::number(testNum));
        if(currentNum == 1 && currentImagePart == 0)
        {
            __ScorePage->ui->plainTextEdit->clear();
            __ScorePage->ui->plainTextEdit->appendPlainText("可以看出，刚才显示的照片的质量很不错");
            __ScorePage->ui->plainTextEdit->appendPlainText("因此您可以去拖动左边的滑块，选择一个较高的分数");
            __ScorePage->ui->plainTextEdit->appendPlainText("例如：");
            __ScorePage->ui->lineEdit->setText("85分");
        }
        else if(currentNum == 2 && currentImagePart == 0)
        {
            __ScorePage->ui->plainTextEdit->clear();
            __ScorePage->ui->plainTextEdit->appendPlainText("可以看出，刚才显示的照片的质量一般");
            __ScorePage->ui->plainTextEdit->appendPlainText("因此您可以去拖动左边的滑块，选择一个中等的分数");
            __ScorePage->ui->plainTextEdit->appendPlainText("例如：");
            __ScorePage->ui->lineEdit->setText("50分");
        }
        else if(currentNum == 3 && currentImagePart == 0)
        {
            __ScorePage->ui->plainTextEdit->clear();
            __ScorePage->ui->plainTextEdit->appendPlainText("可以看出，刚才显示的照片的质量很差");
            __ScorePage->ui->plainTextEdit->appendPlainText("因此您可以去拖动左边的滑块，选择一个较低的分数");
            __ScorePage->ui->plainTextEdit->appendPlainText("例如：");
            __ScorePage->ui->lineEdit->setText("15分");
        }
        else
        {
            __ScorePage->ui->plainTextEdit->clear();
            __ScorePage->ui->plainTextEdit->appendPlainText("你可以根据你的观察给予合适的局部评分");
            __ScorePage->ui->lineEdit->setText("");
        }
        if(currentImagePart ==0)
             __ScorePage->ui->currentPartEdit->setText("整体");
        else
             __ScorePage->ui->currentPartEdit->setText("局部" + QString::number(currentImagePart));
    }
    if (event->key() == Qt::Key_Q)
        close();
}


myPreImageShow::~myPreImageShow()
{
    delete ui;
}

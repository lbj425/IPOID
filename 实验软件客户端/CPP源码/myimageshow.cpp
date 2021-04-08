#include "myimageshow.h"
#include "ui_myimageshow.h"
#include "scorepage.h"
#include "ui_scorepage.h"
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
myImageShow::myImageShow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::myImageShow),timer(new QTimer),__ScorePage(new ScorePage)
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
    ScoreDirPath = "./scores";
    ScanTimePath = "./scantime";
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
void myImageShow::receive_info(QString num,QString path)
{
    Testnumber = num;
    DataDir = path;
    showFullScreen();
    get_image_info();
    one_image_test_get();
    one_image_score();
    QStringList group_split = path.split('/');
    QString group_name = group_split[group_split.size()-1];
    QString save_name = Testnumber + "_" + group_name;
    scantime_save_dir = ScanTimePath + "/" + save_name+".txt";
    score_save_dir =ScoreDirPath + "/"+save_name+".txt";
    ofs_score.open(score_save_dir.toUtf8().data(),std::ios_base::out | std::ios_base::trunc);
    ofs_score.close();
    ofs_scantime.open(scantime_save_dir.toUtf8().data(),std::ios_base::out | std::ios_base::trunc);
    ofs_scantime.close();
}

void myImageShow::iniSignalSlots()
{
    connect(timer,SIGNAL(timeout()),this,SLOT(do_timer_timeout()));
    connect(__ScorePage,SIGNAL(score_signal(int)),this,SLOT(OneImageFinish(int)));
}

void myImageShow::get_image_info()
{
    srand(time(NULL));
    image_dir = DataDir+"/images";
    label_dir = DataDir+"/labels";
    QDir Imagedir(image_dir);
    QDir Labeldir(label_dir);
    //设置文件过滤器
    QStringList nameFilters;
    //设置文件过滤格式
    nameFilters << "*.bmp";
    //将过滤后的文件名称存入到files列表中
    imageList = Imagedir.entryList(nameFilters, QDir::Files|QDir::Readable, QDir::Name);
    labelList = Labeldir.entryList(nameFilters, QDir::Files|QDir::Readable, QDir::Name);
    int Num_total = imageList.size();
    QSet<int> v;
    while(v.size()<3)
    {
       int random_num = rand()%Num_total;
       v.insert(random_num);
        //   qDebug() << random_num;
    }
    for(int i:v)
    {
        imageList.push_back(imageList[i]);
    }
    std::random_shuffle(imageList.begin(), imageList.end());
    testNum = imageList.size();
//    for(int i=0;i<testNum;i++)
//    {
//        qDebug()<< imageList[i];
//    }
//    qDebug()<< testNum;
}
void myImageShow::one_image_test_get()
{
    QString imagePath = image_dir+"/"+imageList[currentNum-1];
    QString image_name_split = imageList[currentNum-1];
    QString image_name = image_name_split.mid(3,2);
    QString label_name = "Label"+image_name+".bmp";
    QString labelPath = label_dir+"/"+label_name;
//    qDebug() << imagePath;
//    qDebug() << image_name;
//    qDebug() << label_name;
//    qDebug() << labelPath;
//    if(!access(labelPath.toUtf8().data(),0))
//    {
//        QMessageBox::information(this,"结束信息框","路径错误："+labelPath);
//        IsRight = false;
//        close();
//        return;
//    }
    while(!img_set.empty())
    {
        img_set.pop_back();
    }
    QImage image(imagePath.toUtf8().data());
    QImage label(labelPath.toUtf8().data());
    int label_y = label.height();
    int label_x = label.width();
    //qDebug()<< image_x;
    //qDebug()<< image_y;
    //qDebug()<< label_x;
    //qDebug()<< label_y;
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
    //qDebug()<< label_count;
    QColor oldColor;
    //QSet<double>::iterator label_it = label_set.begin();
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
        //label_it++;
       // mp.fromImage(newImage);
        img_set.push_back(newImage);
    }
//    for(int i=0;i<label_count+1;i++)
//    {
//        QImage curPixmap = img_set[i];
//        QPixmap p;
//        ui->imageShow->setStyleSheet("background-color:#808080");
//        ui->imageShow->setPixmap(p.fromImage(curPixmap));
//    }
}
void myImageShow::one_image_score()
{
    if(IsRight)
    {
        ui->imageShow->setStyleSheet("background-color:#808080");
        QImage curPixmap = img_set[currentImagePart];
        QPixmap p;
        ui->imageShow->setPixmap(p.fromImage(curPixmap));
        QTime curDataTime = QTime::currentTime();
        ofs_scantime.open(scantime_save_dir.toUtf8().data(),std::ios_base::out | std::ios_base::app);
        ofs_scantime << (imageList[currentNum-1]).toUtf8().data() << "_" << currentImagePart << " "<< curDataTime.toString().toUtf8().data() << std::endl;
        ofs_scantime.close();
   //     IsEnterEnable = false;
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
void myImageShow::do_timer_timeout()
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
       QTime curDataTime = QTime::currentTime();
       ofs_scantime.open(scantime_save_dir.toUtf8().data(),std::ios_base::out | std::ios_base::app);
       ofs_scantime << (imageList[currentNum-1]).toUtf8().data() << "_" << currentImagePart << " "<< curDataTime.toString().toUtf8().data() << std::endl;
       ofs_scantime.close();
       QPixmap curPixmap = QPixmap();
       ui->imageShow->setStyleSheet("background-color:#808080");
       ui->imageShow->setPixmap(curPixmap);
       __ScorePage->ui->finishedEdit->setText(QString::number(currentNum)+"/"+QString::number(testNum));
       if(currentImagePart ==0)
            __ScorePage->ui->currentPartEdit->setText("整体");
       else
            __ScorePage->ui->currentPartEdit->setText("局部" + QString::number(currentImagePart));
    }

}

void myImageShow::OneImageFinish(int score)
{ 
    ofs_score.open(score_save_dir.toUtf8().data(),std::ios_base::out | std::ios_base::app);
    ofs_score << (imageList[currentNum-1]).toUtf8().data() << "_" << currentImagePart << " "<< score << std::endl;
    ofs_score.close();
    IsEnterEnable = false;
    if(currentImagePart == partNum)
    {
        currentImagePart = 0;
        if(currentNum == testNum)
        {
           __ScorePage->close();
           QMessageBox::information(this,"结束信息框","本次测试已经结束，感谢您的参与");
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
void myImageShow::keyPressEvent(QKeyEvent *event)
{
    if(event->key() == Qt::Key_Return && IsEnterEnable == true)
    {
        timer->stop();
        __ScorePage->show();
       QTime curDataTime = QTime::currentTime();
       ofs_scantime.open(scantime_save_dir.toUtf8().data(),std::ios_base::out | std::ios_base::app);
        ofs_scantime << (imageList[currentNum-1]).toUtf8().data() << "_" << currentImagePart << " "<< curDataTime.toString().toUtf8().data() << std::endl;
        ofs_scantime.close();
        QPixmap curPixmap = QPixmap();
        ui->imageShow->setStyleSheet("background-color:#808080");
        ui->imageShow->setPixmap(curPixmap);
        __ScorePage->ui->finishedEdit->setText(QString::number(currentNum)+"/"+QString::number(testNum));
        if(currentImagePart ==0)
             __ScorePage->ui->currentPartEdit->setText("整体");
        else
             __ScorePage->ui->currentPartEdit->setText("局部" + QString::number(currentImagePart));
    }
    if (event->key() == Qt::Key_Q)
        close();
}

myImageShow::~myImageShow()
{
    delete ui;
}

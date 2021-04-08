#include "myinformationdialog.h"
#include "ui_myinformationdialog.h"
#include <QDebug>
#include <QString>
#include <QMessageBox>
#include <fstream>
#include <io.h>
myinformationdialog::myinformationdialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::myinformationdialog)
{
    ui->setupUi(this);
    infopath = ".//information";
    iniSignalSlots();
}

void myinformationdialog::iniSignalSlots()
{
    connect(ui->btnYes,SIGNAL(pressed()),this,SLOT(GetAllInformation()));
    connect(this,SIGNAL(close_event(QString)),this,SLOT(close()));
}

void myinformationdialog::GetAllInformation()
{
    if (ui->nameEdit->text() == "")
     {
        QMessageBox::warning(this,"信息框","未填写姓名");
        return;
     }
    if (ui->ageEdit->text() == "")
     {
        QMessageBox::information(this,"信息框","未填写年龄");
        return;
     }
    if (ui->numberEdit->text() == "")
     {
        QMessageBox::information(this,"信息框","未填写编号");
        return;
     }
    if (ui->majorEdit->text() == "")
     {
        QMessageBox::information(this,"信息框","未填写专业");
        return;
    }
    auto result = QMessageBox::question(this,"信息框","信息填写已完成，是否确认",QMessageBox::Yes|
                                  QMessageBox::Cancel);
    if (result == QMessageBox::Yes)
    {
        QString data_path = infopath+"//"+ui->numberEdit->text()+".txt";
        if(!access(data_path.toUtf8().data(), 0))
        {
            auto result2 = QMessageBox::question(this,"信息框","信息已存在，是否覆盖",QMessageBox::Yes|
                                          QMessageBox::Cancel);
            if(result2== QMessageBox::Cancel)
            {
               QMessageBox::information(this,"信息框","你可以重新填写信息");
               return;
            }
        }
        std::ofstream ofs;
        ofs.open(data_path.toUtf8().data());
        if(!ofs.is_open())
        {
            QMessageBox::information(this,"信息框","文件路径打开失败");
            return;
        }
        ofs << ui->nameEdit->text().toUtf8().data() <<" "<<ui->ageEdit->text().toUtf8().data() << " "
            << ui->numberEdit->text().toUtf8().data() <<" "<<ui->majorEdit->text().toUtf8().data();
        if (ui->manButton->isChecked())
            ofs <<" 男";
        else
            ofs <<" 女";
        ofs.close();
    }
    emit close_event(ui->numberEdit->text());
}
myinformationdialog::~myinformationdialog()
{
    delete ui;
}

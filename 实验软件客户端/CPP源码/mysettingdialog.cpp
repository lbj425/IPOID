#include "mysettingdialog.h"
#include "ui_mysettingdialog.h"
#include <QDebug>
#include <QFileDialog>
#include <QMessageBox>
mySettingDialog::mySettingDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::mySettingDialog)
{
    ui->setupUi(this);
    iniSignalSlots();
}

void mySettingDialog::receive_number(QString num)
{
    number = num;
    show();
}
void mySettingDialog::iniSignalSlots()
{
    connect(ui->btnDirget,SIGNAL(pressed()),this,SLOT(btnDirget_pressed()));
    connect(ui->btnApply,SIGNAL(pressed()),this,SLOT(btnApply_pressed()));
    connect(ui->btnStart,SIGNAL(pressed()),this,SLOT(btnStart_pressed()));
}
void mySettingDialog::btnDirget_pressed()
{
    QString dirStr = QFileDialog::getExistingDirectory();
    if (dirStr == "")
        return;
    ui->lineEdit->setText(dirStr);
}
void mySettingDialog::btnApply_pressed()
{
    DataDir = ui->lineEdit->text();
}
void mySettingDialog::btnStart_pressed()
{
    if(DataDir == "")
    {
        QMessageBox::information(this,"信息框","未填写数据库地址或未点击应用");
        return;
    }
    DataDir = ui->lineEdit->text();
    hide();
    emit beginTest(number,DataDir);
}
mySettingDialog::~mySettingDialog()
{
    delete ui;
}

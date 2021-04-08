#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow),mystartpanel(new MyStartPanel),myinfo(new myinformationdialog),mysettingdlg(new mySettingDialog),myimgshow(new myImageShow),mypreimgshow(new myPreImageShow)
{
    ui->setupUi(this);
    MainWindow::iniSignalSlots();
    mystartpanel->show();
}

void MainWindow::iniSignalSlots()
{
    connect(mystartpanel,SIGNAL(close_event()),myinfo,SLOT(show()));
    connect(myinfo,SIGNAL(close_event(QString)),mysettingdlg,SLOT(receive_number(QString)));
    connect(mysettingdlg,SIGNAL(beginTest(QString,QString)),mypreimgshow,SLOT(receive_info(QString,QString)));
    connect(mypreimgshow,SIGNAL(endpre(QString,QString)),myimgshow,SLOT(receive_info(QString,QString)));
    qDebug() << "链接成功";
}
MainWindow::~MainWindow()
{
    delete ui;
}

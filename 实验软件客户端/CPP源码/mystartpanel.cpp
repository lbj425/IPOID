#include "mystartpanel.h"
#include "ui_mystartpanel.h"
#include "mainwindow.h"
#include <QDebug>
MyStartPanel::MyStartPanel(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::MyStartPanel)
{
    ui->setupUi(this);
    ui->btnEnter->setEnabled(false);
    setWindowFlag(Qt::WindowCloseButtonHint);
    iniSignalSlots();
}
void MyStartPanel::iniSignalSlots()
{
     connect(ui->checkBox,SIGNAL(clicked(bool)),this,SLOT(SetEnterBtnEnabled(bool)));
     connect(ui->btnEnter,SIGNAL(pressed()),this,SIGNAL(close_event()));
     connect(ui->btnEnter,SIGNAL(pressed()),this,SLOT(close()));
}
void MyStartPanel::SetEnterBtnEnabled(bool checked)
{
     ui->btnEnter->setEnabled(checked);
}

MyStartPanel::~MyStartPanel()
{
    delete ui;
}

#include "prescorepage.h"
#include "ui_prescorepage.h"
#include <QDesktopWidget>
PreScorePage::PreScorePage(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::PreScorePage)
{
    ui->setupUi(this);
    ui->finishedEdit->setReadOnly(true);
    ui->currentPartEdit->setReadOnly(true);
    setWindowFlags(Qt::WindowStaysOnTopHint);
    setWindowFlag(Qt::FramelessWindowHint);
    ui->scoreSlider->setTickInterval(20);
    iniSignalSlots();
    QDesktopWidget* desktop = QApplication::desktop(); // =qApp->desktop();也可以
    move((desktop->width() - this->width())/2, (desktop->height() - this->height())/2);
}
void PreScorePage::iniSignalSlots()
{
   connect(ui->btnSure,SIGNAL(clicked()),this,SLOT(emit_Score()));
   connect(ui->scoreSlider,SIGNAL(valueChanged(int)),this,SLOT(scoreSlider_valueChanged(int)));
}
void PreScorePage::scoreSlider_valueChanged(int value)
{
    changeSliderColor();
    ui->scoreEdit->setText(QString::number(value));
}

void PreScorePage::keyPressEvent(QKeyEvent *event)
{
    if(event->key() == Qt::Key_Up)
    {
        int value = ui->scoreSlider->value();
        ui->scoreSlider->setValue(value+1);
    }
    if(event->key() == Qt::Key_Down)
    {
        int value = ui->scoreSlider->value();
        ui->scoreSlider->setValue(value-1);
    }
    if(event->key() == Qt::Key_Control)
        emit_Score();

}
void PreScorePage::emit_Score()
{
    ui->scoreSlider->setValue(50);
    ui->scoreEdit->setText("50");
    hide();
    emit score_signal();
}

void PreScorePage::changeSliderColor()
{
    int num = ui->scoreSlider->value();
    if(num>=0 && num <=20)
    {
        ui->scoreSlider->setStyleSheet("QSlider {\n"
                                            "    padding-top: 15px;\n"
                                            "    padding-bottom: 15px;\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            " \n"
                                            "QSlider::add-page:vertical {\n"
                                            "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f5af19, stop:1 #f12711);\n"
                                            "    width:5px;\n"
                                            "    border-radius: 2px;\n"
                                            "}\n"
                                            " \n"
                                            "QSlider::sub-page:vertical {\n"
                                            "    \n"
                                            "    background-color: rgb(229, 229, 229);\n"
                                            "    width:5px;\n"
                                            "    border-radius: 2px;\n"
                                            "}\n"
                                            " \n"
                                            "QSlider::groove:vertical {\n"
                                            "    background:transparent;\n"
                                            "    width:80px;\n"
                                            "}\n"
                                            " \n"
                                            "QSlider::handle:vertical {\n"
                                            "    height: 20px;\n"
                                            "    width: 20px;\n"
                                            "    margin: 0px -4px 0px -4px;\n"
                                            "    border-radius: 10px;\n"
                                            "    background: rgb(255, 255, 255);\n"
                                            "}");
    }
    else if( num>=20 && num<40)
    {
        ui->scoreSlider->setStyleSheet("QSlider {\n"
                                          "    padding-top: 15px;\n"
                                          "    padding-bottom: 15px;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::add-page:vertical {\n"
                                          "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffff00, stop:1 #f5af19);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::sub-page:vertical {\n"
                                          "    \n"
                                          "    background-color: rgb(229, 229, 229);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::groove:vertical {\n"
                                          "    background:transparent;\n"
                                          "    width:80px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::handle:vertical {\n"
                                          "    height: 20px;\n"
                                          "    width: 20px;\n"
                                          "    margin: 0px -4px 0px -4px;\n"
                                          "    border-radius: 10px;\n"
                                          "    background: rgb(255, 255, 255);\n"
                                          "}");
    }
    else if(num>=40 && num < 60)
    {
        ui->scoreSlider->setStyleSheet("QSlider {\n"
                                          "    padding-top: 15px;\n"
                                          "    padding-bottom: 15px;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::add-page:vertical {\n"
                                          "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #DCE35B, stop:1 #ffff00);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::sub-page:vertical {\n"
                                          "    \n"
                                          "    background-color: rgb(229, 229, 229);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::groove:vertical {\n"
                                          "    background:transparent;\n"
                                          "    width:80px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::handle:vertical {\n"
                                          "    height: 20px;\n"
                                          "    width: 20px;\n"
                                          "    margin: 0px -4px 0px -4px;\n"
                                          "    border-radius: 10px;\n"
                                          "    background: rgb(255, 255, 255);\n"
                                          "}");
    }
    else if(num >=60 && num < 80)
    {
        ui->scoreSlider->setStyleSheet("QSlider {\n"
                                          "    padding-top: 15px;\n"
                                          "    padding-bottom: 15px;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::add-page:vertical {\n"
                                          "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #38ef7d, stop:1 #DCE35B);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::sub-page:vertical {\n"
                                          "    \n"
                                          "    background-color: rgb(229, 229, 229);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::groove:vertical {\n"
                                          "    background:transparent;\n"
                                          "    width:80px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::handle:vertical {\n"
                                          "    height: 20px;\n"
                                          "    width: 20px;\n"
                                          "    margin: 0px -4px 0px -4px;\n"
                                          "    border-radius: 10px;\n"
                                          "    background: rgb(255, 255, 255);\n"
                                          "}");
    }
    else
    {
        ui->scoreSlider->setStyleSheet("QSlider {\n"
                                          "    padding-top: 15px;\n"
                                          "    padding-bottom: 15px;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::add-page:vertical {\n"
                                          "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #11998e, stop:1 #38ef7d);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::sub-page:vertical {\n"
                                          "    \n"
                                          "    background-color: rgb(229, 229, 229);\n"
                                          "    width:5px;\n"
                                          "    border-radius: 2px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::groove:vertical {\n"
                                          "    background:transparent;\n"
                                          "    width:80px;\n"
                                          "}\n"
                                          " \n"
                                          "QSlider::handle:vertical {\n"
                                          "    height: 20px;\n"
                                          "    width: 20px;\n"
                                          "    margin: 0px -4px 0px -4px;\n"
                                          "    border-radius: 10px;\n"
                                          "    background: rgb(255, 255, 255);\n"
                                          "}");
    }

}

PreScorePage::~PreScorePage()
{
    delete ui;
}

#ifndef MYPREIMAGESHOW_H
#define MYPREIMAGESHOW_H

#include <QMainWindow>
#include <QTimer>
#include <QVector>
#include <fstream>
#include "prescorepage.h"
namespace Ui {
class myPreImageShow;
}

class myPreImageShow : public QMainWindow
{
    Q_OBJECT

public:
    explicit myPreImageShow(QWidget *parent = nullptr);
    ~myPreImageShow();
    void get_image_info();
    void one_image_test_get();
    void one_image_score();
    void keyPressEvent(QKeyEvent *event);
    void iniSignalSlots();
signals:
    void endpre(QString,QString);
private slots:
    void receive_info(QString,QString);
    void do_timer_timeout();
    void OneImageFinish();
private:
    Ui::myPreImageShow *ui;
    QString Testnumber;
    QString DataDir;
    int currentNum;
    int currentImagePart;
    QTimer *timer;
    bool IsTestTime;
    bool IsEnterEnable;
    QStringList ScoreList;
    QStringList EyeTrackTime;
    QStringList imageList;
    QStringList labelList;
    QString ScoreDirPath;
    QString ScanTimePath;
    int scantimeAll;
    int scantimePart;
    int scantimeRestPart;
    int scantimeRestAll;
    int restime;
    bool IsRight;
    int testNum;
    QString image_dir;
    QString label_dir;
    QVector<QImage> img_set;
    bool __IfScorePage;
    PreScorePage *__ScorePage;
    int partNum;
};

#endif // MYPREIMAGESHOW_H

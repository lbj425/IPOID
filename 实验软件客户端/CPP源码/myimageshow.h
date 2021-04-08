#ifndef MYIMAGESHOW_H
#define MYIMAGESHOW_H

#include <QMainWindow>
#include <QTimer>
#include <QVector>
#include <fstream>
#include "scorepage.h"
namespace Ui {
class myImageShow;
}

class myImageShow : public QMainWindow
{
    Q_OBJECT

public:
    explicit myImageShow(QWidget *parent = nullptr);
    ~myImageShow();
    void get_image_info();
    void one_image_test_get();
    void one_image_score();
    void keyPressEvent(QKeyEvent *event);
    void iniSignalSlots();
private slots:
    void receive_info(QString,QString);
    void do_timer_timeout();
    void OneImageFinish(int);
private:
    Ui::myImageShow *ui;
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
    ScorePage *__ScorePage;
    int partNum;
    std::ofstream ofs_score;
    std::ofstream ofs_scantime;
    QString score_save_dir;
    QString scantime_save_dir;
};

#endif // MYIMAGESHOW_H

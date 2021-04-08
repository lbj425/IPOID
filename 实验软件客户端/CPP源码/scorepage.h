#ifndef SCOREPAGE_H
#define SCOREPAGE_H

#include <QMainWindow>

namespace Ui {
class ScorePage;
}

class ScorePage : public QMainWindow
{
    Q_OBJECT

public:
    explicit ScorePage(QWidget *parent = nullptr);
    ~ScorePage();
    Ui::ScorePage *ui;
    void keyPressEvent(QKeyEvent *event);
    void changeSliderColor();
signals:
    void score_signal(int);
private slots:
    void emit_Score();
    void scoreSlider_valueChanged(int value);
private:
    void iniSignalSlots();
};

#endif // SCOREPAGE_H

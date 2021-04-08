#ifndef PRESCOREPAGE_H
#define PRESCOREPAGE_H

#include <QMainWindow>

namespace Ui {
class PreScorePage;
}

class PreScorePage : public QMainWindow
{
    Q_OBJECT

public:
    explicit PreScorePage(QWidget *parent = nullptr);
    ~PreScorePage();
    Ui::PreScorePage *ui;
    void keyPressEvent(QKeyEvent *event);
    void changeSliderColor();
signals:
    void score_signal();
private slots:
    void emit_Score();
    void scoreSlider_valueChanged(int value);
private:
    void iniSignalSlots();
};

#endif // PRESCOREPAGE_H

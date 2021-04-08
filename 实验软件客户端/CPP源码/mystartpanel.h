#ifndef MYSTARTPANEL_H
#define MYSTARTPANEL_H

#include <QWidget>

namespace Ui {
class MyStartPanel;
}

class MyStartPanel : public QWidget
{
    Q_OBJECT

public:
    explicit MyStartPanel(QWidget *parent = nullptr);
    ~MyStartPanel();
private slots:
    void SetEnterBtnEnabled(bool checked);

signals:
    void StartPanelClosed();
    void close_event();

private:
    Ui::MyStartPanel *ui;
    void iniSignalSlots();
};

#endif // MYSTARTPANEL_H

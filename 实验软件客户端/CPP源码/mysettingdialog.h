#ifndef MYSETTINGDIALOG_H
#define MYSETTINGDIALOG_H

#include <QDialog>

namespace Ui {
class mySettingDialog;
}

class mySettingDialog : public QDialog
{
    Q_OBJECT

public:
    explicit mySettingDialog(QWidget *parent = nullptr);
    ~mySettingDialog();

private slots:
    void receive_number(QString number);
    void btnDirget_pressed();
    void btnApply_pressed();
    void btnStart_pressed();

signals:
    void beginTest(QString,QString);
private:
    Ui::mySettingDialog *ui;
    QString number;
    QString DataDir;
    void iniSignalSlots();
};

#endif // MYSETTINGDIALOG_H

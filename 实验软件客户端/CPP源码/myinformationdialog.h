#ifndef MYINFORMATIONDIALOG_H
#define MYINFORMATIONDIALOG_H

#include <QDialog>

namespace Ui {
class myinformationdialog;
}

class myinformationdialog : public QDialog
{
    Q_OBJECT

public:
    explicit myinformationdialog(QWidget *parent = nullptr);
    ~myinformationdialog();
signals:
    void close_event(QString number);
private slots:
    void GetAllInformation();
private:
    Ui::myinformationdialog *ui;
    void iniSignalSlots();
    QString infopath;
};

#endif // MYINFORMATIONDIALOG_H

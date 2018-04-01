#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QPushButton>
#include <QDebug>
#include "localserver.h"
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    mLocalServer = new LocalServer(this);

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_exitButton_clicked()
{
    close();

}

void MainWindow::on_submitButton_clicked()
{

    mLocalServer->submit(ui->lineEdit->text());

}

void MainWindow::on_startButton_clicked()
{
    if(!mLocalServer->listen("myLocalServer")){
        QMessageBox::critical(this, "Error", mLocalServer->errorString());
    }
}

#ifndef TEGEN_WINDOWS_H
#define TEGEN_WINDOWS_H

#include <QtCore>
#include <QWidget>
#include <QFrame>
#include <QVector>
#include <QRect>
#include <QColor>
#include <QPainter>
#include <QImage>
#include <QPaintEvent>
#include <QResizeEvent>
#include <QKeyEvent>

typedef struct _tile {
    QRect rect;
    QColor color;
    QImage image;
} tile;

class TegenBoard : public QFrame {
private:
    int seedmod = 0;
    QVector<tile> tiles;

    void init_ui();

public:
    TegenBoard(QWidget *parent = 0);
    
protected:
    void paintEvent(QPaintEvent *e);
    void resizeEvent(QResizeEvent *e);
    void keyPressEvent(QKeyEvent *e);
};

#endif

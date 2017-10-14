#include <cmath>
#include <random>
#include <ctime>

#include "windows.h"

TegenBoard::TegenBoard(QWidget *parent) : QFrame(parent) {
    init_ui();
}

void TegenBoard::init_ui() {
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            if (std::abs(i - 3) + std::abs(j - 3) >= 5)
                continue;
            tile new_tile;
            new_tile.rect.setRect((width() / 7) * i, (height() / 7) * j,
                          width() / 7 - 1, height() / 7 - 1);
            new_tile.color.setRgb(255, 255, 255);

            tiles.append(new_tile);
        }
    }
}

void TegenBoard::paintEvent(QPaintEvent *e) {
    QPainter painter(this);
    painter.setPen(QColor(0, 0, 0));
    for (tile cur : tiles) {
        painter.drawRect(cur.rect);
        painter.fillRect(cur.rect, cur.color);
        if (!cur.image.isNull())
            painter.drawImage(cur.rect, cur.image);
    }
}

void TegenBoard::resizeEvent(QResizeEvent *e) {
    int idx = 0;

    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            if (std::abs(i - 3) + std::abs(j - 3) >= 5)
                continue;

            tiles[idx].rect.setRect((width() / 7) * i, (height() / 7) * j,
                          width() / 7 - 1, height() / 7 - 1);

            idx++;
        }
    }
    update();
}

void TegenBoard::keyPressEvent(QKeyEvent *e) {
    std::mt19937 gen(std::time(NULL) + seedmod);
    std::uniform_int_distribution<int> dist(0, 255);
    seedmod++;

    tiles[e->key() % tiles.length()].color.setRgb(dist(gen), dist(gen), dist(gen));

    update();
}

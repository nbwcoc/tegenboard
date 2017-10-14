#include <QApplication>

#include "windows.h"

int main(int argc, char *argv[]) {
	QApplication app(argc, argv);

	TegenBoard board;

	board.setWindowTitle("Tegen");
	board.show();

	return app.exec();
}

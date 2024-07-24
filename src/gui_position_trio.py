from motor_ctrl.sync_trio import Dynamixel3, MOTOR1_ID, MOTOR2_ID, MOTOR3_ID
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

DEFAULT_VEL = 40

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.dnx = Dynamixel3()
        self.dnx.open_port()
        self.dnx.enable_torque(MOTOR1_ID)
        self.dnx.enable_torque(MOTOR2_ID)
        self.dnx.enable_torque(MOTOR3_ID)

        self.motor_switches = [QCheckBox() for _ in range(4)]
        self.motor_vel_values = [QLineEdit('0') for _ in range(4)]

        self.motor_position_labels = [QLabel('Position: 0', self) for _ in range(3)]

        self.initUI()

    def initUI(self):
        # Create a vertical layout
        layout = QVBoxLayout()

        # Create and add headings
        self.label_rotations = QLabel('Rotations', self)
        self.label_rotations.setAlignment(Qt.AlignCenter)
        self.label_rotations.setStyleSheet("font-size: 14pt; font-weight: bold;")
        layout.addWidget(self.label_rotations)

        # Create buttons
        self.btn_rotate_cw_45 = QPushButton('Rotate CW 45°', self)
        self.btn_rotate_cw_45.setStyleSheet("font-size: 12pt;")
        self.btn_rotate_ccw_45 = QPushButton('Rotate CCW 45°', self)
        self.btn_rotate_ccw_45.setStyleSheet("font-size: 12pt;")
        self.btn_rotate_cw_90 = QPushButton('Rotate CW 90°', self)
        self.btn_rotate_cw_90.setStyleSheet("font-size: 12pt;")
        self.btn_rotate_ccw_90 = QPushButton('Rotate CCW 90°', self)
        self.btn_rotate_ccw_90.setStyleSheet("font-size: 12pt;")

        layout.addWidget(self.btn_rotate_cw_45)
        layout.addWidget(self.btn_rotate_ccw_45)
        layout.addWidget(self.btn_rotate_cw_90)
        layout.addWidget(self.btn_rotate_ccw_90)

        # Create and add heading for translations
        self.label_translations = QLabel('Translations', self)
        self.label_translations.setAlignment(Qt.AlignCenter)
        self.label_translations.setStyleSheet("font-size: 14pt; font-weight: bold;")
        layout.addWidget(self.label_translations)

        self.btn_move_forward = QPushButton('Move Forward 10cm', self)
        self.btn_move_forward.setStyleSheet("font-size: 12pt;")
        self.btn_move_back = QPushButton('Move Back 10cm', self)
        self.btn_move_back.setStyleSheet("font-size: 12pt;")

        # Add buttons to the layout
        layout.addWidget(self.btn_move_forward)
        layout.addWidget(self.btn_move_back)

        # Add motor position labels to the layout
        for i, label in enumerate(self.motor_position_labels):
            layout.addWidget(QLabel(f'Motor {i+1} Position:', self))
            layout.addWidget(label)

        # Connect buttons to the update_values method
        self.btn_rotate_cw_45.clicked.connect(lambda: self.update_values('rotate_cw_45'))
        self.btn_rotate_ccw_45.clicked.connect(lambda: self.update_values('rotate_ccw_45'))
        self.btn_rotate_cw_90.clicked.connect(lambda: self.update_values('rotate_cw_90'))
        self.btn_rotate_ccw_90.clicked.connect(lambda: self.update_values('rotate_ccw_90'))
        self.btn_move_forward.clicked.connect(lambda: self.update_values('move_forward'))
        self.btn_move_back.clicked.connect(lambda: self.update_values('move_back'))

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.start()

        # Set the layout for the main window
        self.setLayout(layout)
        self.setWindowTitle('Robot Control')
        self.resize(400, 400)
        self.show()

    def update_values(self, action):
        if action == 'rotate_cw_45':
            print("Rotating clockwise 45 degrees")
            # Add the corresponding actions here
            self.rotate_cw_45()
        elif action == 'rotate_ccw_45':
            print("Rotating counter-clockwise 45 degrees")
            # Add the corresponding actions here
            self.rotate_ccw_45()
        elif action == 'rotate_cw_90':
            print("Rotating clockwise 90 degrees")
            # Add the corresponding actions here
            self.rotate_cw_90()
        elif action == 'rotate_ccw_90':
            print("Rotating counter-clockwise 90 degrees")
            # Add the corresponding actions here
            self.rotate_ccw_90()
        elif action == 'move_forward':
            print("Moving forward 10 cm")
            # Add the corresponding actions here
            self.move_forward()
        elif action == 'move_back':
            print("Moving back 10 cm")
            # Add the corresponding actions here
            self.move_back()


    def rotate_cw_45(self):

        print("Rotating clockwise 45 degrees")
        motor_id = MOTOR3_ID

        orig_pos = self.dnx.get_position(motor_id)

        new_pos = orig_pos + 1130

        self.dnx.set_position(motor_id, new_pos, DEFAULT_VEL, mode="extpos")


        pos = self.dnx.get_position(motor_id)
        self.motor_position_labels[2].setText(f'Position: {pos}')

        return

    def rotate_ccw_45(self):

        print("Rotating counter-clockwise 45 degrees")
        motor_id = MOTOR3_ID

        orig_pos = self.dnx.get_position(motor_id)

        new_pos = orig_pos - 1130

        self.dnx.set_position(motor_id, new_pos, DEFAULT_VEL, mode="extpos")

        pos = self.dnx.get_position(motor_id)
        self.motor_position_labels[2].setText(f'Position: {pos}')

        return


    def rotate_cw_90(self):
        print("Rotating clockwise 90 degrees")

        motor_id = MOTOR3_ID

        orig_pos = self.dnx.get_position(motor_id)

        new_pos = orig_pos + 2*1130

        self.dnx.set_position(motor_id, new_pos, DEFAULT_VEL, mode="extpos")

        pos = self.dnx.get_position(motor_id)
        self.motor_position_labels[2].setText(f'Position: {pos}')

        return

    def rotate_ccw_90(self):
        print("Rotating counter-clockwise 90 degrees")

        motor_id = MOTOR3_ID

        orig_pos = self.dnx.get_position(motor_id)

        new_pos = orig_pos - 2*1130

        self.dnx.set_position(motor_id, new_pos, DEFAULT_VEL, mode="extpos")

        pos = self.dnx.get_position(motor_id)
        self.motor_position_labels[2].setText(f'Position: {pos}')

        return

    def move_forward(self):

        print("Moving forward by 10cm.")

        for i, motor_id in enumerate([MOTOR1_ID, MOTOR2_ID]):
            orig_pos = self.dnx.get_position(motor_id)

            new_pos = orig_pos + 6910

            self.dnx.set_position(motor_id, new_pos, DEFAULT_VEL, mode="extpos")

        # Update motor position labels
        for i, motor_id in enumerate([MOTOR1_ID, MOTOR2_ID]):
            pos = self.dnx.get_position(motor_id)
            self.motor_position_labels[i].setText(f'Position: {pos}')

        return

    def move_back(self):
        print("Moving back by 10cm.")

        for i, motor_id in enumerate([MOTOR1_ID, MOTOR2_ID]):
            orig_pos = self.dnx.get_position(motor_id)

            new_pos = orig_pos - 6890

            self.dnx.set_position(motor_id, new_pos, DEFAULT_VEL, mode="extpos")

        # Update motor position labels
        for i, motor_id in enumerate([MOTOR1_ID, MOTOR2_ID]):
            pos = self.dnx.get_position(motor_id)
            self.motor_position_labels[i].setText(f'Position: {pos}')


        return

if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    window = MainWindow()
    app.exec_()

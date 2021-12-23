from ai5win_gui import AI5WINArcToolGUI

debug = False


def test(mode: str):
    from ai5win_arc import AI5WINArc
    """modes: unpack, pack,"""
    if mode == "unpack":
        test_arc = AI5WINArc("mes.arc", "mes", integrity_check=True)
        test_arc.unpack()
    elif mode == "pack":
        test_arc = AI5WINArc("mes.arc", "mes", integrity_check=True,
                             first_key=0x5f, second_key=0x46831582, third_key=0x17528913)
        test_arc.pack()


def main():
    gui = AI5WINArcToolGUI()  # Crutch. Otherwise at exit will be shown error.


if __name__ == '__main__':
    if debug:
        test("pack")
    else:
        main()

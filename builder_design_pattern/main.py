from desktop_director import desktopDirector 
from dell_builder import dellBuilder 
from hp_builder import HpBuilder


def main():
    director = desktopDirector() 
    # Build dell desktop
    dell_desktop_builder =  dellBuilder() 
    dell_desktop = director.buildDesktop(dell_desktop_builder) 
    dell_desktop.display()


    print()
    # Build hp desktop 
    hp_dektop_builder = HpBuilder() 
    hp_desktop = director.buildDesktop(hp_dektop_builder) 
    hp_desktop.display()


if(__name__ == "__main__"):
    main()
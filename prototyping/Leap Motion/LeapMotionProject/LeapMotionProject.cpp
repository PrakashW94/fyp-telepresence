// LeapMotionProject.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string.h>
#include <fstream>

#include "custLeap.h"

using namespace std;

int main()
{
	int menu = 0;

	string commands[] =
	{
		"Single Hand Roll",
		"Single Hand Pitch",
		"Single Hand Yaw",
		"Single Hand Height",
		"Single Hand Difference",
		"Grab Strength",
		"Toggle Sensitivity"
	};
	int commandCount = 7;

	while (1)
	{
		//building menu
		cout << "Leap Motion Menu" << endl << endl;
		for (int i = 1; i <= commandCount; i++)
		{
			cout << i << ". " << commands[i - 1] << endl;
		}
		cout << "-1. Quit" << endl;

		cin >> menu;

		switch (menu)
		{
			case 1:
			{
				pollLeap(1); //Roll
				break;
			}

			case 2:
			{
				pollLeap(2); //Pitch
				break;
			}

			case 3:
			{
				pollLeap(3); //Yaw
				break;
			}

			case 4:
			{
				pollLeap(4); //Hand height
				break;
			}

			case 5:
			{
				pollLeap(5); //Hand height
				break;
			}

			case 6:
			{
				pollLeap(6); //Hand height
				break;
			}

			case 7:
			{
				setSensitivity = !setSensitivity;
				cout << "Sensitivity: " << setSensitivity << endl;
				break;
			}

			case -1:
			{
				return 0;
			}

			default: 
			{
				cout << "Invalid Entry!" << endl << endl;
			}
		}
	}
}
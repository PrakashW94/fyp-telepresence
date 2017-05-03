#include "stdafx.h"
#include <iostream>
#include <string.h>
#include <fstream>
#include <chrono>

#include "Leap.h"
#include "custLeap.h"

using namespace Leap;
using namespace std;

ofstream outfile;
bool setSensitivity = true;

const string fingerNames[] = { "Thumb", "Index", "Middle", "Ring", "Pinky" };
const string boneNames[] = { "Metacarpal", "Proximal", "Middle", "Distal" };

int normaliseValue100(float value, float valueRange)
{
	int output = floor((value + (valueRange / float(2))) * (float(100) / valueRange));
	if (output > 100) output = 100;
	if (output < 0) output = 0;
	return output;
}

/*
Input definition
1 - Roll
2 - Pitch
3 - Yaw
4 - Height
*/
void pollLeap(int direction)
{
	Controller controller;
	Frame frame;
	Hand hand;

	int leapFrameRate = 113;

	int64_t lastFrame = 0;
	int newFrames = 0;
	int dupFrames = 0;

	int pretimer = (int) chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now().time_since_epoch()).count();

	int numHands = 0;
	int frameCounter = 0;

	//initialisation loop to run until a single hand is detected over the leap motion over 113 consecutive frames (1 second)
	while (frameCounter < leapFrameRate)
	{
		frame = controller.frame();
		
		if (frame.id() == lastFrame)
		{//old frame, skip
			dupFrames++;
		}
		else
		{//new frame, process
			//process
			lastFrame = frame.id();
			newFrames++;
			//end processing
		 
			//exit condition
			numHands = frame.hands().count();
			if (numHands == 1)
			{
				frameCounter++;
			}
			else
			{
				frameCounter = 0;
			}
			//end exit condition

			//frame report
			//cout << "New frame found: " << frame.id() << " vs. " << lastFrame << endl;
			cout << "Searching for hands... ";// << endl;
			cout << '\r';
			//end frame report

		}
	}

	frameCounter = 0;

	//main loop to run until no hand is detected over the leap motion over 113 consecutive frames
	while (frameCounter < leapFrameRate)
	{
		frame = controller.frame();
		
		if (frame.id() == lastFrame)
		{//old frame, skip
			dupFrames++;
		}
		else
		{//new frame, process

			//processing
			if (frame.hands().count() == 1)
			{ //only process if 1 hand in frame
				lastFrame = frame.id();
				newFrames++;
				hand = frame.hands()[0];

				switch (direction)
				{
					case 1: //Roll
					{
						if (setSensitivity)
						{
							float roll = hand.palmNormal().roll() * RAD_TO_DEG;
							int outputRoll = normaliseValue100(roll, 120);
							cout << "Roll: " << outputRoll << endl;
						}
						else
						{
							cout << "Roll: " << hand.palmNormal().roll() * RAD_TO_DEG << endl;
						}

						break;
					}

					case 2: //Pitch
					{
						cout << "Pitch: " << hand.direction().pitch() * RAD_TO_DEG << endl;
						break;
					}

					case 3: //Yaw
					{
						cout << "Yaw: " << hand.direction().yaw() * RAD_TO_DEG << endl;
						break;
					}

					case 4: //Palm Height
					{
						cout << "Height: " << hand.palmPosition().y << endl;
						break;
					}
					case 5: //Difference in all?
					{
						Hand lastHand = controller.frame(1).hands()[0];
						//lastHand.
						float dRoll, dPitch, dYaw, dHeight;
						dRoll = (lastHand.palmNormal().roll() - hand.palmNormal().roll()) * RAD_TO_DEG;
						dPitch = (lastHand.direction().pitch() - hand.direction().pitch()) * RAD_TO_DEG;
						dYaw = (lastHand.direction().yaw() - hand.direction().yaw()) * RAD_TO_DEG;
						dHeight = (lastHand.palmPosition().y - hand.palmPosition().y);

						cout << "R: " << dRoll << ", P: " << dPitch << ", Y: " << dYaw << ", H: " << dHeight << endl;
						break;
					}

					case 6: //Pinch or grab
					{
						cout << "Grab Strength: " << hand.grabStrength() << endl;
						break;
					}
				}

			}
			//end processing

			//exit condition
			numHands = frame.hands().count();
			if (numHands == 0)
			{
				frameCounter++;
			}
			else
			{
				frameCounter = 0;
			}
			//end exit condition
			
			//report
			/*
			cout << "New frame found: " << frame.id() << " vs. " << lastFrame << endl;
			cout << "Frame counter: " << frameCounter << endl;
			*/
			//end report
		}
	}

	int posttimer = (int) chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now().time_since_epoch()).count();

	int timer = posttimer - pretimer;
	float frameRate = (float) newFrames / (timer / 1000);

	//report
	cout << endl << endl;
	cout << "Duplicate Frames Processed: " << dupFrames << endl;
	cout << "New Frames Processed: " << newFrames << endl;
	cout << "Time Elapsed (ms): " << timer << endl;
	cout << "Frame Rate (FPS): " << frameRate << endl;
	cout << endl << endl;
}
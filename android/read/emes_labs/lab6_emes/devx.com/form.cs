// In the code-behind of Form1, import the following namespaces:
using System;
using System.Windows.Forms;
using System.IO;
// Define the following member variable:
namespace LBS
{
    public partial class Form1 : Form
    {
        Timer t;
        //---log file for CellID data---
        const string FILE_NAME = @"\CellIDs.txt";
        StreamWriter sw;
/*
Because you're invoking the GetCellTowerInfo() method only periodically, you'll use a Timer object to do so. Also, all the CellIDs you obtain will be logged in a text file for processing later.

In the Form1 constructor, add the following line of code:
*/
		public Form1()
		{
			InitializeComponent();
			sw = new StreamWriter(FILE_NAME, true, 
				System.Text.Encoding.ASCII);
		}
/*
In the Form1_Load event handler, initialize the Timer object, and wire up the event handler for the Tick event:
*/
		private void Form1_Load(object sender, EventArgs e)
		{
			t = new Timer() { 
				Interval = 2000,   //---fired every 2 seconds
				Enabled = true 
			};
			t.Tick += new EventHandler(t_Tick);
		}
/*
In the Tick event's handler, you will obtain the CellID of the device by calling the the RIL class's GetCellTowerInfo() static method. This displays the CellID and the current time in the Label control, and simultaneously logs the information into the text file:
*/
		void t_Tick(object sender, EventArgs e)
		{
			string cellid = RIL.GetCellTowerInfo();
			string txt = cellid + "-" + DateTime.Now.ToString();

			//---display in textbox control---
			lblCellID.Text = txt;

			//---write to file---           
			sw.WriteLine(txt);
			sw.Flush();
		}
/*
The Start menu's item control has a Click event handler that enables the Timer object to trigger the Tick event every two seconds:

Figure 2. Located! Displaying the CellID information obtained by the device.
*/
		private void mnuStart_Click(object sender, EventArgs e)
		{
			t.Enabled = true;
			sw = new StreamWriter(FILE_NAME, true, 
				System.Text.Encoding.ASCII);
		}
}
/*
Likewise, the Stop menu's item control also has a Click event handler that disables the Timer object: 
private void mnuStop_Click(object sender, EventArgs e) { t.Enabled = false; sw.Close(); } 
That's it! Press F5 to deploy the application onto a Windows Mobile Professional device 
(remember to ensure that you have a valid SIM card). Figure 2 shows the CellID information 
you've obtained. Notice that, as you move from one location to another, the CellID information may change).
*/

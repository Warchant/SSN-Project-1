/*
When the user clicks the Load Cell IDs button, load the log file containing the CellIDs and display them in the ListBox control: 
*/ 
 private void btnLoadCellIDs_Click(object sender, EventArgs e)
{
	OpenFileDialog openFileDialog1 = new OpenFileDialog()
	{
		Filter = "Text files (*.txt)|*.txt"
	};

	if (openFileDialog1.ShowDialog() == DialogResult.OK)
	{
		System.IO.StreamReader sr =
		System.IO.File.OpenText(openFileDialog1.FileName);
		string strCellIDs = sr.ReadToEnd();
		string[] cellIDs = strCellIDs.Split('\n');
		foreach (string str in cellIDs)
		{
			lstCellIDs.Items.Add(str.Replace('\r', ' '));
		}
	}
}

/*		
Listing 4.  
Set the WebBrowser control to navigate to the Google Maps application by feeding the latitude and longitude information in the query string.  
*/
private void lstCellIDs_SelectedIndexChanged(object sender, EventArgs e)
{
	string[] cellidFields = lstCellIDs.SelectedItem.ToString().Split('-');
	// [0] - CID 
	// [1] - LAC
	// [2] – MCC
	// [3] - Time

	//---Arguments for GetLatLng(MCC MNC LAC CID)---
	string[] args = { 
		cellidFields[2], // MCC 
		"0",             // MNC – don’t need it here
		cellidFields[1], // LAC
		cellidFields[0]  // CID
	};

	string[] latlng = GMM.GetLatLng(args).Split('|');

	webBrowser1.Navigate(
		   "http://maps.google.com/maps?hl=en&q=" +
		   latlng[0].ToString().Replace(',', '.') +
		   "," + latlng[1].ToString().Replace(',', '.') +
		   "&ie=UTF8");
}
	
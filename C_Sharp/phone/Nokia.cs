public class Nokia : Phone, IRingable 
{
    public Nokia(string versionNumber, int batteryPercentage, string carrier, string ringTone) 
        : base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring() 
        {
            string ringer = "Banana phoooooooooooooooooooooner";
            return ringer;
        }
        public string Unlock() 
        {
            string swipe = "Nokia has been unlocked!!";
            return swipe;
        }
        public override void DisplayInfo() 
        {
            // your code here            
        }
}
        
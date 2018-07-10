public class Nokia : Phone, IRingable 
{
    public Nokia(string versionNumber, int batteryPercentage, string carrier, string ringTone) 
        : base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring() 
        {
            return "Banana phoooooooooooooooooooooner";
        }
        public string Unlock() 
        {
            return "Nokia has been unlocked!!";
        }
        public override void DisplayInfo() 
        {
            System.Console.WriteLine("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");
            System.Console.WriteLine("Nokia: "+_versionNumber);
            System.Console.WriteLine("Battery Percentage: "+_batteryPercentage);
            System.Console.WriteLine("Carrier: "+_carrier);
            System.Console.WriteLine("Ring Tone: "+_ringTone);
            System.Console.WriteLine("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");            
        }
}
        
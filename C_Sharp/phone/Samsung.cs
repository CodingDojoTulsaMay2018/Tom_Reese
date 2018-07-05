    public class Galaxy : Phone, IRingable 
    {
        public Galaxy(string versionNumber, int batteryPercentage, string carrier, string ringTone) 
            : base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring() 
        {
            return ringTone;
        }
        
        public string Unlock() 
        {
            // return ;
        }
        public override void DisplayInfo() 
        {
            // your code here            
        }
}
        
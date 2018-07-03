namespace classes {
    public class Vehicle {
        public int numPassengers;
        public double distance; 

        public Vehicle(int val = 0, double odo) {
            numPassengers = val;
            distance = odo;
        }

        public int Move(double miles)
        {
            distance += miles;
            return (int)distance;
        }
        public int Move(double miles, bool km)
        {
            // Convert the KM measurement to miles
            if (km == true)
            {
                miles = miles * 0.62;
            }
            return Move(miles);
        }
    }
}
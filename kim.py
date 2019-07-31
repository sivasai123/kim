 return ((sr - floor(sr)) == 0); 
} 
  
int main() { 
  long double x = 2500; 
  if (isPerfectSquare(x)) 
    cout << "Yes"; 
  else
    cout << "No"; 
  return 0; 
}  

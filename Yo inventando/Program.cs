///Proyecto calcuLEIROOOOOL en SIchalP (C sharp)

Console.WriteLine("*******************************");
Console.WriteLine("****Calculadora Básica v1.0****");
Console.WriteLine("*******************************");
Console.WriteLine("Elige una operación");
Console.WriteLine("1. Suma | 2. Resta | 3. Multiplicación | 4. División");
int Eleccion = int.Parse(Console.ReadLine()!);
if(Eleccion==1)
{
    Console.WriteLine("Escribe el n1");
    double n1 = double.Parse(Console.ReadLine()!);
    Console.WriteLine("Escribe el n2");
    double n2 = double.Parse(Console.ReadLine()!);
    double resultado = n1+n2;
    Console.WriteLine("EL resultado es: "+ resultado);  
}
else if(Eleccion==2)
{
    Console.WriteLine("Escribe el n1");
    double n1 = double.Parse(Console.ReadLine()!);
    Console.WriteLine("Escribe el n2");
    double n2 = double.Parse(Console.ReadLine()!);
    double resultado = n1-n2;
    Console.WriteLine("EL resultado es: "+resultado);
}
else if(Eleccion == 3)
{
    Console.WriteLine("Escribe el n1");
    double n1 = double.Parse(Console.ReadLine()!);
    Console.WriteLine("Escribe el n2");
    double n2 = double.Parse(Console.ReadLine()!);
    double resultado = n1*n2;
    Console.WriteLine("EL resultado es: "+resultado);
}
else if(Eleccion==4)
{
    Console.WriteLine("Escribe el n1");
    double n1 = double.Parse(Console.ReadLine()!);
    Console.WriteLine("Escribe el n2");
    double n2 = double.Parse(Console.ReadLine()!);
    if(n2==0)
    {
        Console.WriteLine("Opción inválida, intenta usar otro número");
    }
    double resultado = n1/n2;
    Console.WriteLine("EL resultado es: "+resultado);
    
}
else
{
    Console.WriteLine("Error de elección, inténtalo más tarde");
}
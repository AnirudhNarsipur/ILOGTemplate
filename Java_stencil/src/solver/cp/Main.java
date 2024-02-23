package solver.cp;

import ilog.concert.IloException;

import ilog.cp.IloCP;

import java.io.FileNotFoundException;

import java.io.IOException;

import java.nio.file.Path;
import java.nio.file.Paths;

public class Main
{  
  public static void main(String[] args) throws FileNotFoundException, IOException, IloException
  {
	
	Timer watch = new Timer();
	CPInstance instance = new CPInstance();
	
    watch.start();
    instance.solveAustraliaGlobal();
    watch.stop();
     
  }
}

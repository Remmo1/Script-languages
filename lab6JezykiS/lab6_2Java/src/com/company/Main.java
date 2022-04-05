package com.company;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    private static final String FILENAME = "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab6JezykiS/lab6_2Java/covid.txt";

    public static void openFile(String fileName, String country, int month) {
        String line;
        String[] tokens;
        int actual;
        int sumN = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            while ( ( line = br.readLine() ) != null ) {
                tokens = line.split("\t");
                actual = 0;

                if (tokens[6].equals(country)) {
                    try {
                        if (Integer.parseInt(tokens[2]) == month)
                            actual = Integer.parseInt(tokens[4]);
                    }
                    catch(Exception ignored) {
                    }

                    sumN += actual;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Suma dla miesiaca " + month + " dla kraju " + country + " : " + sumN);
    }

    public static void main(String[] args) {

        /*
        Scanner sc = new Scanner(System.in);

        System.out.print("Podaj nazwe kraju: ");
        String country = sc.next();

        System.out.print("Podaj numer miesiaca (od 1 do 12): ");
        int month = sc.nextInt();

         */

        try {
            openFile(FILENAME, args[0], Integer.parseInt(args[1]));
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}

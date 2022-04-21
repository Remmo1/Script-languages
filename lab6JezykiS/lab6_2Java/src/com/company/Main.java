package com.company;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    private static final String FILENAME_UBUNTU = "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab6JezykiS/covid.txt";
    private static final String FILENAME_WINDOWS = "C:\\Uczelnia\\Semestr4\\Jezyki Skryptowe\\laby\\lab6JezykiS\\covid.txt";

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
        try {
            openFile(FILENAME_WINDOWS, args[0], Integer.parseInt(args[1]));
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Blad! Sprobuj ponownie, musisz podac dokladnie 2 argumenty w linii konsoli");
        }
    }
}

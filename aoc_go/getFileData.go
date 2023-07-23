package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	// Get the current working directory
	currentDir, err := os.Getwd()
	if err != nil {
		fmt.Println("Error getting the current working directory:", err)
		return
	}

	// Specify the name of the folder containing the file
	folderName := "input"

	// Create the full path to the file
	fileName := filepath.Join(currentDir, "..", folderName, "01.txt")

	// Open the file in read-only mode
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Error opening the file:", err)
		return
	}
	defer file.Close()

	// Create a scanner to read the file line by line
	scanner := bufio.NewScanner(file)

	// Read the file line by line
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line) // Do whatever you want with the line read from the file
	}

	// Check for any errors occurred during reading
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading the file:", err)
	}
}

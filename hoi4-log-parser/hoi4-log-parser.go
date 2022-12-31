package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	fmt.Println("########## Starting")

	csvFile, err := os.Create("csv.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer csvFile.Close()

	// head of csv table
	header := "country_tag,fuel_amount,day,manpower_amount,number_armies,heavy_tank_divs,amount_infantry_equipment,light_tank_divs,medium_tank_divs,number_ships"
	_, errCsv := csvFile.WriteString(header)
	if errCsv != nil {
		log.Fatal(err)
	}

	file, err := os.Open("./game_logging.log")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	const maxCapacity = 10240 * 1024
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	csvLine := ""
	for scanner.Scan() {
		line := scanner.Text()

		if strings.HasPrefix(line, "end ===") {
			// marks end of entry
			// insert into csv file here
			_, errCsv := csvFile.WriteString(csvLine)
			if errCsv != nil {
				log.Fatalf("Failed to add line to csv")
			}
			csvLine = ""

		} else if strings.HasPrefix(line, "283original_tag") {
			// get country tag, since names change, only the tag can be used
			value := getValueFromParenthesis(line)
			csvLine = "\n" + value + csvLine

		} else if strings.HasPrefix(line, "283") {
			var value string

			// check if string is saved as province
			if strings.Contains(line, "(") {
				value = getValueFromParenthesis(line)
			} else {
				line = strings.ReplaceAll(line, " ", "")
				variableLine := strings.Split(line, "=")
				value = variableLine[1]
			}

			csvLine = csvLine + "," + value
		}
	}
	fmt.Println("########## Done")
}

// get value of line in parenthesis
// low values in the game dont get printed as the value itself, but as the province that has the
// number assigned to it
func getValueFromParenthesis(line string) string {
	line = strings.ReplaceAll(line, " ", "")
	pair := strings.Split(line, "=")
	values := strings.Split(pair[1], "(")
	value := strings.ReplaceAll(values[1], ")", "")
	return value
}

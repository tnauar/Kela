# This program will write a 5000 row csv data file that contains random
# imaginary person data.

# This sources contains the constants from which the data is created.
source("./constants_person.R")

# Main program starts here.
# We will loop 5000 times and for each round we will generate a random
# data containing person data and write it to memory to a data frame.
random_data_results <- data.frame(
  firstname = character(),
  lastname = character(),
  nationality = character(),
  education = character(),
  gender = character(),
  situation = character()
)

for (i in 1:5000) {
  
  # On each round random value is chosen for each variable.
  # In some cases there might be probability weights in order
  # to make the data a bit more realistic.
  gender <- sample(
    c("M","N","T"),
    1,
    prob = c(0.5, 0.49, 0.01)
  )
  
  if (gender == "M") {
    firstname = sample(
      FIRST_NAMES_MALE,
      1
    )
  }  
  else if (gender == "N") {
    firstname = sample(
      FIRST_NAMES_FEMALE,
      1
    )
  }
  # For trans or no gender we choose randomly from both names.
  else {
    firstname = sample(
      c(FIRST_NAMES_MALE, FIRST_NAMES_FEMALE),
      1
    )
  }
  
  lastname <- sample(
    LAST_NAMES,
    1
  )
  
  situation <- sample(
    CUSTOMER_SITUATION,
    1
  )

  
  education <- sample(
    EDUCATION,
    1
  )
  
  nationality <- sample(
    NATIONALITY,
    1,
    prob = c(0.90, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01)
  )
  
  row <-data.frame(  
                  firstname,
                  lastname,
                  nationality,
                  education,
                  gender,
                  situation

  )
  random_data_results <- rbind(random_data_results, row)
  
# End of for-loop  
}

# Finally we will write the data from the memory to a csv file.

write.csv(random_data_results, "person_data.csv")



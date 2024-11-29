Start
1. Import Modules
 * random for generating random numbers.
 * sys for handling command-line arguments.
 * datetime for timestamps in result files.
 * Custom game function from MYGAMEFUNCTION.
2. Command-Line Arguments
 * Parse arguments (sys.argv).
   * If none provided, default to Demo mode.
   * If arguments exist:
     * -e: Set mode to Easy.
     * -m: Set mode to Medium.
     * -h: Set mode to Hard.
 * Display the chosen game mode.
3. Initialize Game Setup
 * Generate a unique filename combining date, time, and random number (e.g., 20241129_1035_123.txt).
 * Open the result file in write mode and add current date and time.
 * Initialize session counter to track game sessions played.
4. Game Loop
 * Increment session number at each session start.
 * Display the session number to the user.
 * Call MYGAMEFUNCTION.game(arg, file) to conduct a math quiz:
   * arg: Difficulty level (Demo, Easy, Medium, Hard).
   * game function generates problems, validates input, and writes results to the file.
   * Each session includes:
     * Math questions.
     * User answers.
     * Correct answers.
     * Scored marks.
 * Record session details in the file:
   * Session number.
   * Total questions, correct answers, and percentage score.
   * Difficulty mode chosen.
 * Ask the user if they want to play again:
   * "yes" restarts the loop.
   * "no" exits the loop.
5. End Game
 * Close the result file.
 * Display a thank-you message: "Thank you for playing Math-Bro!".
 * Exit the program.
Sub-Algorithms
Function cal_answer (Calculating the Correct Answer):
 * Inputs:
   * n1: First number.
   * n2: Second number.
   * ope: Operator (+, -, *).
 * Calculation:
   * Based on ope:
     * +: return n1 + n2.
     * -: return n1 - n2.
     * *: return n1 * n2.
Function game (Conducting the Math Quiz):
 * Inputs:
   * mode: Difficulty level (Demo, Easy, Medium, Hard).
   * file: Opened result file for saving session details.
 * Define Parameters:
   * Demo Mode:
     * 3 questions.
     * Operators: +.
     * Number range: 0–5.
   * Easy Mode:
     * 5 questions.
     * Operators: +, -.
     * Number range: 0–10.
   * Medium Mode:
     * 10 questions.
     * Operators: +, -.
     * Number range: 0–10.
   * Hard Mode:
     * 10 questions.
     * Operators: +, -, *.
     * Number range: 0–20.
 * Display Number of Questions: Inform the user about the number of questions.
 * Initialize Variables:
   * num1_list, num2_list: Lists to store generated numbers.
   * operator_list: List to store operators.
   * user_answer_list: List to store user responses.
   * correct_answer_list: List to store correct answers.
   * correct_count: Counter for correct responses.
 * Loop Through Questions:
   * Generate random numbers and operator based on the mode.
   * Display the question and accept the user's answer.
   * Validate the user's answer:
     * If correct, increment correct_count.
     * If incorrect, display the correct answer.

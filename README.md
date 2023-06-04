<h1>Typing Test</h1>

<p>This command-line program allows you to practice your typing skills by generating random words and measuring your typing speed and accuracy.</p>

<h2>Features</h2>
<ul>
  <li>Choose between local JSON words or API-generated words</li>
  <li>Specify the number of words you want to practice with</li>
  <li>Measure your typing speed (WPM) and accuracy</li>
</ul>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.x</li>
  <li>requests library (<code>pip install requests</code>)</li>
</ul>

<h2>Usage</h2>
<ol>
  <li>Clone the repository or download the <code>main.py</code> file.</li>
  <li>Open a terminal and navigate to the directory where <code>main.py</code> is located.</li>
  <li>Run the script using the following command:</li>
</ol>

<pre><code>python main.py</code></pre>

<p>Select the desired option by entering the corresponding number:</p>

<ul>
  <li><strong>Option 1</strong>: Local JSON Words
    <ul>
      <li>Enter the number of words you want to practice with.</li>
      <li>Start typing the displayed words.</li>
    </ul>
  </li>
  <li><strong>Option 2</strong>: API Generated Words
    <ul>
      <li>Enter the number of words you want to practice with.</li>
      <li>Random words will be fetched from an API.</li>
      <li>Start typing the displayed words.</li>
    </ul>
  </li>
  <li><strong>Option 3</strong>: Exit the program.</li>
</ul>

<h2>Example</h2>

<pre>
<code>(1) Local JSON Words
(2) API Generated Words
(3) Exit

::: 1
How many words would you like: 10

Press Enter to start typing...

apple orange banana cat dog tiger elephant lion bear
Enter the text above: apple orange banana cat dog tiger elephant lion bear

Correct: 10/10
Accuracy: 100.00%
WPM: 60.00
</code>
</pre>

<h2>Contributing</h2>

<p>Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

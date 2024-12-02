<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Command Output to HTML Converter</title>
</head>
<body>
    <header>
        <h1>Command Output to HTML Converter</h1>
        <p>This Python script runs shell commands and converts the command output to an HTML document format.</p>
    </header>

    <section>
        <h2>Features</h2>
        <ul>
            <li>Runs shell commands using Python's <code>subprocess</code> module.</li>
            <li>Converts the output into a simple, clean HTML format.</li>
            <li>Saves the HTML output to a file for easy viewing in a browser.</li>
        </ul>
    </section>

    <section>
        <h2>Installation</h2>
        <p>Follow the steps below to set up the script:</p>
        <ol>
            <li><strong>Clone this repository</strong> (or download the Python script):
                <pre><code>git clone https://github.com/yourusername/command-output-to-html.git</code></pre>
            </li>
            <li><strong>Navigate to the directory</strong> where the script is saved:
                <pre><code>cd command-output-to-html</code></pre>
            </li>
            <li><strong>Ensure Python 3 is installed</strong>. The script is compatible with Python 3.7+.</li>
        </ol>
    </section>

    <section>
        <h2>Usage</h2>
        <h3>Running the Script</h3>
        <p>To run the script, simply execute it from the command line:</p>
        <pre><code>python cmd_to_html.py</code></pre>
        <p>By default, the script will run the command <code>echo Hello, this is a test command!</code> and save the output as an HTML file.</p>

        <h3>Customizing the Command</h3>
        <p>To run your own command and convert its output to HTML, modify the <code>command</code> variable inside the script or pass the command as an argument.</p>
        <p>For example, open the <code>cmd_to_html.py</code> script and modify the <code>command</code> variable:</p>
        <pre><code>command = "ls -l"</code></pre>
        <p>Then, run the script:</p>
        <pre><code>python cmd_to_html.py</code></pre>

        <h3>Output</h3>
        <p>The generated HTML file will contain the command output wrapped in a <code>&lt;pre&gt;</code> tag. Here's an example of what the HTML will look like:</p>
        <pre><code>
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Command Output&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Command Output&lt;/h1&gt;
    &lt;pre&gt;Hello, this is a test command!&lt;/pre&gt;
&lt;/body&gt;
&lt;/html&gt;
        </code></pre>
        <p>The output file will be saved as <code>command_output.html</code> in the same directory.</p>
    </section>

    <section>
        <h2>Code Explanation</h2>
        <h3>1. Running the Command</h3>
        <p>The <code>run_command()</code> function uses Python's <code>subprocess</code> module to run shell commands.</p>
        <p>The <code>subprocess.run()</code> function captures both the standard output and the error output from the shell command.</p>

        <h3>2. Converting Output to HTML</h3>
        <p>The <code>convert_to_html()</code> function takes the output of the shell command and formats it into HTML.</p>
        <p>It wraps the command output inside a <code>&lt;pre&gt;</code> tag to preserve its formatting.</p>

        <h3>3. Saving the HTML File</h3>
        <p>The <code>save_html()</code> function saves the generated HTML to a file, <code>command_output.html</code>.</p>

        <h3>Python Code:</h3>
        <pre><code>
import subprocess
import os

def run_command(command):
    """ Run the shell command and capture its output. """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e.stderr}"

def convert_to_html(command_output):
    """ Convert the command output into a simple HTML format. """
    html_content = f"""
    &lt;!DOCTYPE html&gt;
    &lt;html lang="en"&gt;
    &lt;head&gt;
        &lt;meta charset="UTF-8"&gt;
        &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
        &lt;title&gt;Command Output&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;Command Output&lt;/h1&gt;
        &lt;pre&gt;{command_output}&lt;/pre&gt;
    &lt;/body&gt;
    &lt;/html&gt;
    """
    return html_content

def save_html(html_content, filename="command_output.html"):
    """ Save the HTML content to a file. """
    with open(filename, "w") as file:
        file.write(html_content)
    print(f"HTML file saved as {filename}")

if __name__ == "__main__":
    # Example command to run
    command = "echo Hello, this is a test command!"
    
    # Run the command
    command_output = run_command(command)
    
    # Convert the output to HTML format
    html_content = convert_to_html(command_output)
    
    # Save the result as an HTML file
    save_html(html_content)
        </code></pre>
    </section>

    <footer>
        <p>© 2024 Command Output to HTML Converter. All rights reserved.</p>
    </footer>
</body>
</html>

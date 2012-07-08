# Description

Whitespace highlighting for Sublime Text 2.

![Options Screenshot](https://github.com/gorte/ST2-Whitespaces/raw/master/example.png)

# Allows to:

1. Highlight tabs and spaces
2. Highlight line endings
3. Show line ending icon in the gutter
4. Show line ending type in the status bar

# Options

See Whitespaces.sublime-settings

# Changing Colors

You can define your own scopes in your theme file, for example:

	<dict>
		<key>name</key>
		<string>Whitespaces.space</string>
		<key>scope</key>
		<string>Whitespaces.space.highlight</string>
		<key>settings</key>
   		<dict>
   			<key>background</key>
   			<string>#232323</string>
   			<key>fontStyle</key>
   			<string></string>
   			<key>foreground</key>
   			<string>#ffffff</string>
   		</dict>
	</dict>
	<dict>
		<key>name</key>
		<string>Whitespaces.tab</string>
		<key>scope</key>
		<string>Whitespaces.tab.highlight</string>
		<key>settings</key>
   		<dict>
   			<key>background</key>
   			<string>#1c2a2d</string>
   			<key>fontStyle</key>
   			<string></string>
   			<key>foreground</key>
   			<string>#ffffff</string>
   		</dict>
	</dict>
	<dict>
		<key>name</key>
		<string>Whitespaces.line_ending</string>
		<key>scope</key>
		<string>Whitespaces.line_ending.highlight</string>
		<key>settings</key>
   		<dict>
   			<key>background</key>
   			<string>#3e1111</string>
   			<key>fontStyle</key>
   			<string></string>
   			<key>foreground</key>
   			<string>#eda24c</string>
   		</dict>
	</dict>

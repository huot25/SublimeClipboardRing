# SublimeClipboardRing

The SublimeClipboardRing plugin adds functionality similar to Visual Studio's Clipboard Ring feature. Leveraging the `Paste from History` functionality available in Sublime Text 3, the plugin will allow a user to iterate through the clipboard stack using a mapped key binding. This eliniates the need to press multiple key combinations to bring up a list of the clipboard stack to select an item to insert into the file.

## Usage

Simply press the mapped key combination to cycle through the clipboard stack.

### Keybinding

I have purposefully ommitted the key bindings as this should be defined by the user. Simply add the following JSON entry to your User Key Binding file to enable the feature.

```json

	{ "keys": ["ctrl+shift+insert"], "command": "cycle_clipboard" }

```
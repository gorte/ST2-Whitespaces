from os.path import exists, join, normpath
import sublime, sublime_plugin

WS_DEFAULT_MAX_FILE_SIZE = 1048576
WS_DEFAULT_HIGHLIGHT_SCOPE_NAME = 'invalid'
WS_DEFAULT_SHOW_WHITESPACES_ON_MINIMAP = True
WS_DEFAULT_HIGHLIGHT_LINE_ENDINGS = True
WS_DEFAULT_SHOW_LINE_ENDINGS_IN_STATUS_BAR = True
WS_DEFAULT_SHOW_LINE_ENDINGS_IN_GUTTER = True
WS_DEFAULT_ICON_PATH = 'Theme - Default'

ws_settings = sublime.load_settings('Whitespaces.sublime-settings')

def ws_toggle_spaces(view, pattern, region_key, highlight_scope_name):
    old_highlight = view.get_regions(region_key)
    if len(old_highlight):
        view.erase_regions(region_key)
    else:
        show_whitespaces_on_minimap = ws_settings.get('show_whitespaces_on_minimap', WS_DEFAULT_SHOW_WHITESPACES_ON_MINIMAP)
        regions = view.find_all(pattern)
        view.add_regions(region_key, regions, highlight_scope_name, sublime.DRAW_EMPTY | 0 if show_whitespaces_on_minimap else sublime.HIDE_ON_MINIMAP)

def ws_toggle_line_endings(view):
    show_line_endings_in_status_bar = ws_settings.get('show_line_endings_in_status_bar', WS_DEFAULT_SHOW_LINE_ENDINGS_IN_STATUS_BAR)
    status_key = 'ws_line_endings_status'
    region_key = 'ws_line_endings_highlight'
    old_highlight = view.get_regions(region_key)
    if len(old_highlight):
        view.erase_regions(region_key)
        show_line_endings_in_status_bar and view.set_status(status_key, '')
    else:
        highlight_scope_name = ws_settings.get('line_ending_highlight_scope_name', WS_DEFAULT_HIGHLIGHT_SCOPE_NAME)
        highlight_line_endings = ws_settings.get('highlight_line_endings', WS_DEFAULT_HIGHLIGHT_LINE_ENDINGS)
        show_line_endings_in_gutter = ws_settings.get('show_line_endings_in_gutter', WS_DEFAULT_SHOW_LINE_ENDINGS_IN_GUTTER)
        line_endings = view.line_endings()
        icon = ''
        if show_line_endings_in_gutter:
            if line_endings == 'Windows':
                icon_type = 'crlf'
            elif line_endings == 'Unix':
                icon_type = 'lf'
            else:
                icon_type = 'cr'
            icon_name = ws_settings.get(icon_type + '_icon', '')
            icon_path = ws_settings.get('icon_path', WS_DEFAULT_ICON_PATH).replace('\\', '/').strip('/')
            if exists(normpath(join(sublime.packages_path(), icon_path, icon_name + '.png'))):
                icon = '../%s/%s' % (icon_path, icon_name)
        regions = view.find_all("\n")
        view.add_regions(region_key, regions, highlight_scope_name, icon, sublime.DRAW_EMPTY if highlight_line_endings else sublime.HIDDEN)
        show_line_endings_in_status_bar and view.set_status(status_key, line_endings)

class WsToggleSpacesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        max_file_size = ws_settings.get('max_file_size', WS_DEFAULT_MAX_FILE_SIZE)
        if view.size() <= max_file_size:
            space_highlight_scope_name = ws_settings.get('space_highlight_scope_name', WS_DEFAULT_HIGHLIGHT_SCOPE_NAME)
            tab_highlight_scope_name = ws_settings.get('tab_highlight_scope_name', space_highlight_scope_name)
            if tab_highlight_scope_name == space_highlight_scope_name:
                ws_toggle_spaces(view, "[\t ]+", 'ws_spaces_highlight', space_highlight_scope_name)
            else:
                ws_toggle_spaces(view, " +", 'ws_spaces_highlight', space_highlight_scope_name)
                ws_toggle_spaces(view, "\t+", 'ws_tabs_highlight', tab_highlight_scope_name)

class WsToggleLineEndingsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        max_file_size = ws_settings.get('max_file_size', WS_DEFAULT_MAX_FILE_SIZE)
        if view.size() <= max_file_size:
            ws_toggle_line_endings(view)

class WsToggleWhitespacesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        view.run_command('ws_toggle_spaces')
        view.run_command('ws_toggle_line_endings')

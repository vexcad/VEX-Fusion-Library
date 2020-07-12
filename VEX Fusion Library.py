import os
import sys
import adsk.core
import traceback

app_path = os.path.dirname(__file__)

sys.path.insert(0, app_path)
sys.path.insert(0, os.path.join(app_path, 'apper'))

try:
    import config
    import apper

    # Basic Fusion 360 Command Base samples
    from .commands.SampleCommand1 import SampleCommand1
    from .commands.SampleCommand2 import SampleCommand2
    from .commands.ModifyPart import ModifyPart
    from .commands.BetterJoint import BetterJoint
    from .commands.SetAttributes import SetAttributes
    from .commands.ViewAttributes import ViewAttributes

    # Palette Command Base samples
    from .commands.SamplePaletteCommand import SamplePaletteSendCommand, SamplePaletteShowCommand

    # Various Application event samples
    from .commands.SampleCustomEvent import SampleCustomEvent1
    from .commands.SampleDocumentEvents import SampleDocumentEvent1, SampleDocumentEvent2
    from .commands.SampleWorkspaceEvents import SampleWorkspaceEvent1
    from .commands.SampleWebRequestEvent import SampleWebRequestOpened
    from .commands.SampleCommandEvents import SampleCommandEvent


# Create our addin definition object
    addin = apper.FusionApp(config.app_name, config.company_name, False)

    # # Creates a basic Hello World message box on execute
    # addin.add_command(
    #     'Sample Command 1',
    #     SampleCommand1,
    #     {
    #         'cmd_description': 'Hello World!',
    #         'cmd_id': 'sample_cmd_1',
    #         'workspace': 'FusionSolidEnvironment',
    #         'toolbar_panel_id': 'Commands',
    #         'cmd_resources': 'command_icons',
    #         'command_visible': True,
    #         'command_promoted': False,
    #     }
    # )

    # # General command showing inputs and user interaction
    # addin.add_command(
    #     'Sample Command 2',
    #     SampleCommand2,
    #     {
    #         'cmd_description': 'A simple example of a Fusion 360 Command with various inputs',
    #         'cmd_id': 'sample_cmd_2',
    #         'workspace': 'FusionSolidEnvironment',
    #         'toolbar_panel_id': 'Commands',
    #         'cmd_resources': 'command_icons',
    #         'command_visible': True,
    #         'command_promoted': False,
    #     }
    # )

    addin.add_command(
        'Modify Part',
        ModifyPart,
        {
            'cmd_description': 'Modify parametric parts from the VEX Fusion 360 Library.\n\nSelect part component and change parameters.',
            'cmd_id': 'modify_part',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Build',
            'cmd_resources': 'modify_part',
            'command_visible': True,
            'command_promoted': True,
        }
    )

    addin.add_command(
        'Better Joint',
        BetterJoint,
        {
            'cmd_description': 'An easier to use joint tool for connecting VEX parts',
            'cmd_id': 'better_joint',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Build',
            'cmd_resources': 'better_joint',
            'command_visible': True,
            'command_promoted': True,
        }
    )

    addin.add_command(
        'Set Attributes',
        SetAttributes,
        {
            'cmd_description': 'Set custom attributes for parts from the VEX Fusion 360 Library.\n\nSelect part component and input valid JSON string.',
            'cmd_id': 'set_attributes',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Advanced',
            'cmd_resources': 'set_attributes',
            'command_visible': True,
            'command_promoted': True,
        }
    )

    addin.add_command(
        'View Attributes',
        ViewAttributes,
        {
            'cmd_description': 'View custom attributes for parts from the VEX Fusion 360 Library.',
            'cmd_id': 'view_attributes',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Advanced',
            'cmd_resources': 'view_attributes',
            'command_visible': True,
            'command_promoted': True,
        }
    )

    # # Create an html palette to as an alternative UI
    # addin.add_command(
    #     'Sample Palette Command - Show',
    #     SamplePaletteShowCommand,
    #     {
    #         'cmd_description': 'Shows the Fusion 360 Demo Palette',
    #         'cmd_id': 'sample_palette_show',
    #         'workspace': 'FusionSolidEnvironment',
    #         'toolbar_panel_id': 'Palette',
    #         'cmd_resources': 'palette_icons',
    #         'command_visible': True,
    #         'command_promoted': True,
    #         'palette_id': 'sample_palette',
    #         'palette_name': 'Sample Fusion 360 HTML Palette',
    #         'palette_html_file_url': 'palette_html/VEX Fusion Library.html',
    #         'palette_is_visible': True,
    #         'palette_show_close_button': True,
    #         'palette_is_resizable': True,
    #         'palette_width': 500,
    #         'palette_height': 600,
    #     }
    # )

    # # Send data from Fusion 360 to the palette
    # addin.add_command(
    #     'Send Info to Palette',
    #     SamplePaletteSendCommand,
    #     {
    #         'cmd_description': 'Send data from a regular Fusion 360 command to a palette',
    #         'cmd_id': 'sample_palette_send',
    #         'workspace': 'FusionSolidEnvironment',
    #         'toolbar_panel_id': 'Palette',
    #         'cmd_resources': 'palette_icons',
    #         'command_visible': True,
    #         'command_promoted': False,
    #         'palette_id': 'sample_palette',
    #     }
    # )

    app = adsk.core.Application.cast(adsk.core.Application.get())
    ui = app.userInterface

    # Uncomment as necessary.  Running all at once can be overwhelming :)
    # addin.add_custom_event("VEX Fusion Library_message_system", SampleCustomEvent1)

    # addin.add_document_event("VEX Fusion Library_open_event", app.documentActivated, SampleDocumentEvent1)
    # addin.add_document_event("VEX Fusion Library_close_event", app.documentClosed, SampleDocumentEvent2)

    # addin.add_workspace_event("VEX Fusion Library_workspace_event", ui.workspaceActivated, SampleWorkspaceEvent1)

    # addin.add_web_request_event("VEX Fusion Library_web_request_event", app.openedFromURL, SampleWebRequestOpened)

    # addin.add_command_event("VEX Fusion Library_command_event", app.userInterface.commandStarting, SampleCommandEvent)

except:
    app = adsk.core.Application.get()
    ui = app.userInterface
    if ui:
        ui.messageBox('Initialization: {}'.format(traceback.format_exc()))

# Set to True to display various useful messages when debugging your app
debug = False


def run(context):
    addin.run_app()


def stop(context):
    addin.stop_app()
    sys.path.pop(0)
    sys.path.pop(0)

#: import demo demo.demo

<MessageScreen>:

    MDBoxLayout: 
        orientation: "vertical"
        md_bg_color: app.theme_cls.bg_normal
        MDToolbar: 
            id: logoToolBar
            height: 50
            title: "Whatsapp"
            right_action_items: [['dots-vertical', lambda x: app.show_theme_picker()]]
            margin: 0

        ScrollView:
            do_scroll_y: True
            effect_cls: 'ScrollEffect'
            bar_width: 0
            MDBoxLayout:
                adaptive_height: True
                orientation: 'vertical'
                md_bg_color: app.theme_cls.primary_color
                spacing: 20
                MDBoxLayout:
                    height: 60
                    size_hint_y: None
                    ScrollView:
                        do_scroll_x: True
                        do_scroll_y: False
                        bar_width: 0
                        MDBoxLayout: 
                            id: story_layout
                            orientation: 'horizontal'
                            adaptive_width: True
                            spacing: 10
                            padding: [10, 0, 0, 0]
                            StoryWithIcon:

                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: app.theme_cls.bg_normal
                    size_hint_y: None
                    adaptive_height: True
                    radius: [20, 20, 0, 0]
                    padding: [0, 0, 0, 40]
                    MDList:
                        id: chatlist
                        spacing: 10
    MDBoxLayout:
        size_hint_y: None
        md_bg_color: 0, 0, 0, 0
        NavBar:
            one: [1, 1, 1, 1]
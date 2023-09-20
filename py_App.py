from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8,alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(
                top_left=35,
                top_right=0,
                bottom_left=35,
                bottom_right=0
        )
        page_2.update()
        
    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(
            1,alignment=alignment.center_right)
        page_2.update()
    

    
    create_task_view = Container(on_click= lambda _:page.go('/'),
        content=Container(width=40, height=40,
                          content=Text('X'))
    )
    
    tasks=Column(
        height=400,
        scroll='auto',
        # controls=[
        #     Container(width=300,height=50,bgcolor='red'),
        #     Container(width=300,height=50,bgcolor='red'),
        #     Container(width=300,height=50,bgcolor='red'),
        #     Container(width=300,height=50,bgcolor='red'),
        # ]
    )
    for i in range(10):
        tasks.controls.append(
            Container(width=400,height=70,
                      bgcolor=BG,border_radius=20,
                      padding=padding.only(left=20, top=25),
                      content=CustomCheckBox(PINK,
                                             size=30,
                                             label= 'Create interesting content!'
                                             ))
        )
    
    categories_card = Row(
        scroll='auto'
    )
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate (categories):
        categories_card.controls.append(
            Container(
                bgcolor=BG,
                height=110,
                width=170,
                border_radius=20,
                padding= 15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )
            )
        )
    
    first_page_contents= Container(
        content=Column(
            controls=[
                Row(alignment = 'spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                            content=Icon(
                                icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Text(
                    value = 'What\'s Up Muzzamil'
                ),
                Text(
                    value= 'CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content= categories_card
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(bottom=2, right=20,
                            icon = icons.ADD,on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
            
        ),
    )
    page_1 = Container(
        width= 400,
        height= 850,
        border_radius=35,
        bgcolor=BG,
        padding=padding.only(left=50,
                             right=200,
                             top=60),
        
        content=Column(
            controls=[
                Row(alignment = MainAxisAlignment.END,
                    controls=[
                        Container(
                            padding=padding.only(left=13,
                                                 top=13),
                            border_radius=25,
                            height=50,
                            width=50,
                            border=border.all(color='white', width=1),
                            on_click=lambda e: restore(e),
                            content=Text('<')
                        )
                    ]
                ),
                Text('Salam\nMalhub',size=32, weight='bold'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white60'),
                    Text('Templates',size=15,weight=FontWeight.W_300,
                         color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL, color='white60'),
                    Text('Templates',size=15,weight=FontWeight.W_300,
                         color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED, color='white60'),
                    Text('Templates',size=15,weight=FontWeight.W_300,
                         color='white',font_family='poppins')
                ]),
            ]
        )
    )
    page_2 = Row(alignment = 'end',
        controls=[
            Container(
                width= 400,
                height= 850,
                border_radius=35,
                bgcolor= FG,
                animate = animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale = animation.Animation(400, curve='decelerate'),
                padding= padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )
    
    container = Container(
        width= 400,
        height= 850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    pages = {
        '/':View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ],
        )
    }
    
    def route_change(route):
      page.views.clear()
      page.views.append(
          pages[page.route]
      )
    
    page.on_route_change = route_change
    page.go(page.route)


app(target=main)

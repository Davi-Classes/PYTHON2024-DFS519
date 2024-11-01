import db
import flet as ft
from typing import Callable


def Task(
    id: int, 
    name: str, 
    completed: bool, 
    on_delete: Callable[[int], None], 
    on_change_status: Callable[[int], None]
) -> ft.Row:
    return ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Checkbox(name, completed, on_change=lambda _: on_change_status(id)),
            ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color=ft.colors.RED,
                on_click=lambda _: on_delete(id)
            )
        ]
    )

def main(page: ft.Page):
    page.title = 'To Do - Infinity'

    tasks_view = ft.Column()
    task_input = ft.TextField(hint_text='Insira sua tarefa...')

    def list_tasks():
        tasks_view.controls.clear()
        
        for task in db.tasks:
            tasks_view.controls.append(
                Task(
                    task.get('id'), 
                    task.get('name'), 
                    task.get('completed'),
                    on_delete_task,
                    on_change_task_status
                )
            )
        
        page.update()

    def on_save_task(event: ft.ControlEvent):
        task = {
            'id': db.new_id(),
            'name': task_input.value, 
            'completed': False,
        }
        db.tasks.append(task)

        list_tasks()
        task_input.value = ''

    def on_delete_task(id: int):
        for i, task in enumerate(db.tasks):
            if task.get('id') == id:
                db.tasks.pop(i)
        
        list_tasks()

    def on_change_task_status(id: int):
        for task in db.tasks:
            if task.get('id') == id:
                task['completed'] = not task['completed']
        

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    'Tarefas', 
                    style=ft.TextThemeStyle.HEADLINE_MEDIUM
                ),
                ft.Row(
                    controls=[
                        task_input,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD,
                            on_click=on_save_task
                        )
                    ]
                ),
                tasks_view
            ]
        )
    )

    list_tasks()


if __name__ == '__main__':
    ft.app(target=main)

#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    freq_arg = DeclareLaunchArgument(
        'publish_frequency',           # имя аргумента
        default_value='8.0',          # значение по умолчанию
        description='Частота публикации чётных чисел (Гц)'
    )

    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='80',
        description='Порог, после которого происходит переполнение'
    )
    name_arg = DeclareLaunchArgument(
        'publisher_name',
        default_value='even_pub',
    )
    listener_arg = DeclareLaunchArgument(
            'listener_name',
            default_value='overflow_listener',
    )
    topic_arg = DeclareLaunchArgument(
                'numbers_topic',
                default_value='/even_numbers',
    )
    overflow_arg = DeclareLaunchArgument(
                    'overflow_topic',
                    default_value='/overflow',
        )
    # Получаем текущее значение аргумента
    frequency = LaunchConfiguration('publish_frequency')
    threshold = LaunchConfiguration('overflow_threshold')
    name = LaunchConfiguration('publisher_name')
    listener = LaunchConfiguration('listener_name')
    topic = LaunchConfiguration('numbers_topic')
    overflow = LaunchConfiguration('overflow_topic')
    return LaunchDescription([
        freq_arg,          # не забудь добавить аргумент сюда!
        threshold_arg,
        name_arg,
        listener_arg,
        topic_arg,
        overflow_arg,
        Node(
            package='super_Kirill1_study_pkg',
            executable='even_pub',
            name=name,
            parameters=[
                {'publish_frequency': frequency},   # используем аргумент
                {'overflow_threshold': threshold},
                {'topic_name': topic},
            ],
            remappings =[
                ('overflow', overflow)
            ],
            output='screen',
        ),
        Node(
            package='super_Kirill1_study_pkg',
            executable='overflow_listener',
            name=listener,
            remappings =[
                ('overflow', overflow)
            ],
            output='screen',
        )
    ])
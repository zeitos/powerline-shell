def add_root_indicator_segment():
    bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG
    main_prompt = ' \\$ '
    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG
        main_prompt = u' ✘ '
    
    root_indicators = {
        'bash': ' \\$ ',
        'zsh': main_prompt,
        'bare': ' $ ',
    }
    shell = root_indicators[powerline.args.shell]
    powerline.append(shell, fg, bg)

add_root_indicator_segment()

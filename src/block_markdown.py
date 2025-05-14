def markdown_to_blocks(markdown):
    # Split the markdown into lines
    blocks = markdown.split("\n\n")

    for i, block in enumerate(blocks):
        block = block.strip('\n')
        block = block.strip()
        blocks[i] = block

    for block in blocks:
        if not block:        
            blocks.remove(block)
            continue

    return blocks
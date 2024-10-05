### 1. Marcovchain with state size 1
- very random output

### 2. Marcovchain with state 2-3
- beatiful output
- turns out just copy pasting poems
    - wrote a plagarising checker with 10-grams

### 3. went back to state size 1, no(less) copy pasting but too meaningless

### 4. Tried to add randomeness with avoiding overlps of certain size
- at first we tought that the vopy pasting issue is solvd but we managed to caught copy pasting by lovering the n-gram checker. 

### 5. When max_overlap is smaller it still gets 4-grams from different opems but chains them in a rather meaningfull way.
- only certain meet the constraints, so a bit repetitive


tries=20000,
max_overlap_ratio=0.6,  # Allow only up to 50% overlap
max_overlap_total=3   # Allow overlap of up to 10 words


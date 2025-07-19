# Setup Example 

For UNIX like OS (MacOS, Linux, Solaris etc.) -> hints for Wintendo boxes

## Cloning Repository

<kbd>git clone https://github.com/SchrodtSven/hca</kbd>

<kbd>cd hca</kbd>



## VENV

### Install virtual environment
<code>sven@Thanos hca% </code><kbd>python3 -m venv .venv</kbd>

### Activate virtual environment
<code>sven@Thanos hca% </code><kbd>source .venv/bin/activate</kbd>

<code><span style="color:green">(.venv)</span> sven@Thanos hca% </code>

#### For Wintendo:

```PS
.venv\Scripts\activate
```

## Resolving dependencies 

<code><span style="color:green">(.venv)</span> sven@Thanos hca% </code><kbd>pip -r req.txt</kbd>

## App start
Bootstrappping with  ```STDIN``` and ```STDOUT``` to ```dev/null```

```sh
(.venv) svenschrodt@Thanos hca% python app.py > /dev/null  2>&1 &
```

#### For Wintendo:

```PS
Z:\hca> py.exe app.py
```
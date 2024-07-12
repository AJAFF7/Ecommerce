# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

###export LOLCAT="lolcat"


export JAVA_HOME=/opt/jdk-21.0.3
export PATH=$JAVA_HOME/bin:$PATH

#export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64

#export PATH=$JAVA_HOME/bin:$PATH



# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"





alias dps='sudo docker ps --format="ID\t{{.ID}}\nNAME\t{{.Names}}\nIMAGE\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"'

alias d0="sudo systemctl stop docker"
alias d0s="sudo systemctl stop docker.service docker.socket"
alias d1="sudo systemctl start docker"
alias ds="sudo systemctl status docker"
alias di="sudo docker images"
alias dp="dps"
alias dstop="sudo docker stop"
alias dstart="sudo docker start"

alias a="ansible-playbook -i inventory"

alias j0="sudo systemctl stop jenkins"
alias j1="sudo systemctl start jenkins"
alias jr="sudo systemctl restart jenkins"
alias js="sudo systemctl status jenkins"
#alias jsa="sudo journalctl -u snap.jenkins.jenkins"

#Generals
alias port="sudo netstat -anp tcp | grep "
alias c="clear"

alias os="lsb_release -dirc"

#alias m="free -h"
#alias df="df -h"
#alias dfs="df -h | grep shm"

alias dr="sudo systemctl daemon-reload"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


#Usefull Command
#sudo chmod 600 /etc/netplan/01-network-manager-all.yaml
#sudo ip -s -s neigh flush all
#sudo arp-scan --interface=enp0s1 192.168.1.0/24

#sudo dhclient -v -r eth0
#sudo dhclient -v eth0
#lxc exec Ubuntu -- bash -c 'sudo ip addr add 10.227.253.10/24 dev eth0'
alias pst="pstree -p"


#LXD
alias lxd0="sudo systemctl stop snap.lxd.daemon"
alias lxd0s="sudo systemctl stop snap.lxd.daemon.unix.socket"
alias lxd1="sudo systemctl start snap.lxd.daemon"
alias lxdr="sudo systemctl restart snap.lxd.daemon"
alias lxds="systemctl status snap.lxd.daemon"



#location of image copy
alias lc="lc_l"
lc_l() {
    sudo sh -c "cd /var/snap/lxd/common/lxd/storage-pools/JFpool/images/ && exec \$SHELL"
}


#LXC
alias lxcil="sudo lxc image list"
alias lxcsl="sudo lxc storage list"
alias lxcssp="sudo lxc storage show JFpool"
alias lxcnl="sudo lxc network list"
alias lxcnc="sudo lxc network edit lxdbr0"
#alias lxcl="sudo lxc list"
alias lxcrl="sudo lxc remote list"

alias lxc0=" sudo lxc stop Ubuntu"
alias lxc1="sudo lxc start Ubuntu"
alias lxcr="sudo lxc restart Ubuntu"
alias lxcsx="sudo lxc status Ubuntu"
alias lxce="sudo lxc exec Ubuntu -- bash"
alias lxcinf="sudo lxc info Ubuntu"
alias U="sudo lxc exec Ubuntu -- /bin/bash"
alias lxc50=" sudo lxc exec Ubuntu -- cat /etc/netplan/50-cloud-init.yaml"
alias lxcc="lxc config show Ubuntu | less"
alias lxcp="lxc profile show default"
alias lxcm="lxc config set Ubuntu limits.memory"

#Zpool
alias zpth="sudo zpool status -v JFpool"
alias zc="sudo zpool create Jpool /var/snap/lxd/common/lxd/disks/Jpool.img"
alias zdist="sudo zpool destroy"
alias zs="sudo zpool status -v JFpool"
alias zdf="sudo zfs list -o space -r JFpool"
alias zclone="sudo zfs list -t clone -r JFpool"
alias zl="sudo zpool list"

#MicroK8s
alias m0="sudo microk8s stop"
alias m1="sudo microk8s start"
alias ms="sudo systemctl status snap.microk8s.daemon-kubelite.service"
alias me="sudo systemctl enable snap.microk8s.daemon-kubelite.service"
alias md="sudo systemctl disable snap.microk8s.daemon-kubelite.service"



#Snap snapshot
alias ss="sudo snap saved"
alias sf="sudo snap forget"



#Swap
#alias swap="sudo swapon --show"
alias swapoff="sudo swapoff /swapfile"
alias swapon="sudo swapon /swapfile"

#alias swapoff="sudo swapoff -a"
#alias swapon="sudo swapon -a"



## Add temporary swap space
#sudo fallocate -l 2G /tempswap
#sudo mkswap /tempswap
#sudo swapon /tempswap

## Turn off the original swap file
#sudo swapoff /swapfile

## Clean and re-enable the original swap file
#sudo swapon /swapfile

## Remove temporary swap space
#sudo swapoff /tempswap
#sudo rm /tempswap

          


###
log_1() {
    if [ -s /var/log/cleaner/Apt-Cleaner/clean_apt.log ]; then
        sudo cat /var/log/cleaner/Apt-Cleaner/clean_apt.log
    else
        echo -e "\e[38;5;214mNo logs found in Apt-Cleaner\e[0m"
    fi
}

alias log-1='log_1'



###
log_2() {
    local logs_found=false
    
    for log_file in /var/log/cleaner/Caches-Cleaner/drop_caches_1.log /var/log/cleaner/Caches-Cleaner/drop_caches_2.log; do
        if [ -s "$log_file" ]; then
            sudo cat "$log_file"
            logs_found=true
        fi
    done

    if ! $logs_found; then
        echo -e "\e[38;5;214mNo logs found in Caches-Cleaner\e[0m"
    fi
}

alias log-2='log_2'



###
log_3() {
    local log_files=(
        "/var/log/cleaner/Systems-Cleaner/cron_cache_clean.log"
        "/var/log/cleaner/Systems-Cleaner/cron_journalctl.log"
        "/var/log/cleaner/Systems-Cleaner/cron_tmp_clean.log"
    )
    
    local any_logs_found=false
    local orange_color="\033[38;2;255;165;0m" # RGB for orange
    local reset_color="\033[0m"

    for log_file in "${log_files[@]}"; do
        if [ -s "$log_file" ]; then
            sudo cat "$log_file"
            any_logs_found=true
        fi
    done

    if [ "$any_logs_found" = false ]; then
        echo -e "${orange_color}No logs found in any of the specified log files${reset_color}"
    fi
}

alias log-3='log_3'




###
log_4() {
    local log_file="/var/log/cleaner/Processes/process_cleanup.log"
    local orange_color="\033[38;2;255;165;0m" # RGB for orange
    local reset_color="\033[0m"
    
    if [ -s "$log_file" ]; then
        sudo cat "$log_file"
    else
        echo -e "${orange_color}No logs found in Processes${reset_color}"
    fi
}

alias log-4='log_4'




log_9() {
    local log_file="/var/log/cleaner/Update-Repository/apt_update.log"
    local num_packages_found=false
    local all_packages_updated=false
    
    if [ -f "$log_file" ]; then
        # Use awk to find the first occurrence of "All packages are up to date" to detect no upgrades available
        all_packages_updated=$(awk '/All packages are up to date/ {print $0}' "$log_file")
        
        if [ -n "$all_packages_updated" ]; then
            echo -e "\e[32m All Packages Updated Successfully \xe2\x9c\x93\e[0m"
            return
        fi
        
        # Use awk to find the first occurrence of "packages can be upgraded" and extract the number of packages
        local num_packages=$(awk '/packages can be upgraded/ && !found {print $1; found=1}' "$log_file")
        
        if [ -n "$num_packages" ] && ! $num_packages_found; then
            num_packages_found=true
            echo -e "\e[31m Packages Need to Be Upgraded: $num_packages \xe2\x9c\x97\e[0m"
        fi
    fi
    
    if ! $num_packages_found && ! $all_packages_updated; then
        echo -e "\e[32m All Packages Updated Successfully \xe2\x9c\x93\e[0m"
    fi
}

alias log-9="log_9"



function MEM() {
   "$@" | lolcat
}
alias m="MEM free -h"


function SWAP() {
   "$@" | lolcat
}
alias swap="SWAP sudo swapon --show"   



function DISK() {
    "$@" | lolcat
}
alias mp="DISK mpstat -P ALL"


function CPU() {
    "$@" | lolcat
}
alias df="CPU df -h"


function Update() {
    "$@" | lolcat
}
alias ud="Update sudo apt update"


function Update() {
    "$@" | lolcat
}
alias ug="Update sudo apt upgrade"


function LXD() {
    "$@" | lolcat
}
alias lxcl="LXD sudo lxc list"



function DFS() {
    "$@" | lolcat
}
alias dfsh="DFS df -h | grep shm"












alias drop1='sudo sh -c '\''echo 1 > /proc/sys/vm/drop_caches && echo "$(date): \e[37mCache level\e[0m \e[31m2\e[0m \e[32mdropped successfully\e[0m" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'' && sudo sh -c '\''echo 2 > /proc/sys/vm/drop_caches && echo "$(date): \e[37mCache level\e[0m \e[31m1\e[0m \e[32mdropped successfully\e[0m" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'' && sudo sh -c '\''echo 3 > /proc/sys/vm/drop_caches && echo "$(date): \e[37mCache level\e[0m \e[31m3\e[0m \e[32mdropped successfully\e[0m" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'



alias drop2='sudo sh -c '\''sync; echo 1 > /proc/sys/vm/drop_caches && echo "$(date): \e[37mCache level\e[0m \e[31m2\e[0m \e[32mdropped successfully\e[0m" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'' && sudo sh -c '\''sync; echo 2 > /proc/sys/vm/drop_caches && echo "$(date): \e[37mCache level\e[0m \e[31m1\e[0m \e[32mdropped successfully\e[0m" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'' && sudo sh -c '\''sync; echo 3 > /proc/sys/vm/drop_caches && echo "$(date): \e[37mCache level\e[0m \e[31m3\e[0m \e[32mdropped successfully\e[0m" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'















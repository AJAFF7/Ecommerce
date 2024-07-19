#If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

###export LOLCAT="lolcat"

export PATH=/usr/bin:$PATH


export JAVA_HOME=/opt/jdk-21.0.3
export PATH=$JAVA_HOME/bin:$PATH


# Enable fzf key bindings
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Enable fzf auto-completion
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh





# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"


plugins=(git zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh


# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion



alias dps='sudo docker ps --format="ID\t{{.ID}}\nNAME\t{{.Names}}\nIMAGE\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"'

alias d0="sudo systemctl stop docker"
alias d0s="sudo systemctl stop docker.service docker.socket"
alias d1="sudo systemctl start docker"
alias d="sudo systemctl status docker"
alias di="sudo docker images"
alias dp="dps"
alias dstop="sudo docker stop"
alias dstart="sudo docker start"
alias ld="lazydocker"

#Kubernetes
alias kgp="kubectl get pods"
alias kgd="kubectl egt deployments"
alias kgs="kubectl get svc"
alias kga="kubectl get all"

alias k-0="kubectl config use-context kind-cluster-0"
alias k-1="kubectl config use-context kind-cluster-1"
alias kc="kubectl config current-context"


alias a="ansible-playbook -i inventory"

#Jenkins
alias j0="sudo systemctl stop jenkins"
alias j1="sudo systemctl start jenkins"
alias jr="sudo systemctl restart jenkins"
alias j="sudo systemctl status jenkins"
#alias jsa="sudo journalctl -u snap.jenkins.jenkins"


#Grafana
alias g0="sudo systemctl stop grafana-server"
alias g1="sudo systemctl start grafana-server"
alias gr="sudo systemctl restart grafana-server"
alias g="sudo systemctl status grafana-server"

#Loki
alias l0="sudo systemctl stop loki"
alias l1="sudo systemctl start loki"
alias lr="sudo systemctl restart loki"
alias l="sudo systemctl status loki"



#Promtail
alias p0="sudo systemctl stop promtail"
alias p1="sudo systemctl start promtail"
alias pr="sudo systemctl restart promtail"
alias p="sudo systemctl status promtail"



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

          

alias f="fzf"

alias f="find / -type f 2>/dev/null | fzf --preview='batcat --color=always {}'"

#alias fp="fzf --preview='batcat --color=always {}'" 

#alias fp="code $(fzf --preview='batcat --color=always {}')"

# Function to interactively kill a process
fk() {
  local pid
  pid=$(ps aux | fzf --prompt "Select process to kill: " --header "Press 'Enter' to kill, 'Ctrl+C' to cancel" | awk '{print $2}')
  if [[ -n "$pid" ]]; then
    echo "Killing process $pid"
    kill -9 "$pid"
  else
    echo "No process selected"
  fi
}






# Function to change directory using fzf, searching the entire filesystem
fcd() {
  local dir
  dir=$(find / -type d 2>/dev/null | fzf --prompt "● Select directory: " --height 40% --preview "echo {}" --preview-window=up:30%:hidden)
  if [[ -n "$dir" ]]; then
    cd "$dir" || return
    echo "Changed directory to $(pwd)"
  else
    echo "No directory selected"
  fi
}







###
log_1() {
    if [ -s /var/log/cleaner/Apt-Cleaner/clean_apt.log ]; then
        sudo cat /var/log/cleaner/Apt-Cleaner/clean_apt.log
    else
        echo -e "\e[38;5;214mNo logs found in Apt-Cleaner \xe2\x9c\x93\e[0m"
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
        echo -e "\e[38;5;214mNo logs found in Caches-Cleaner \xe2\x9c\x93\e[0m"
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



#alias log-10='source /var/log/cleaner/Update-Repository/apt_update.sh && log_9'





function SWAP() {
   "$@" | lolcat
}
alias swap="SWAP sudo swapon --show"   

function MEM() {
   "$@" | lolcat
}
alias ml="MEM free -h"

function CPU() {
    "$@" | lolcat
}
alias mpl="CPU mpstat -P ALL"


function DISK() {
    "$@" | lolcat
}
alias dfl="DISK df -h --exclude-type=fuse.gvfsd-fuse"


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











#Generals
alias port="sudo netstat -anp tcp | grep "
alias c="clear"
alias R="sudo reboot"
alias os="lsb_release -dirc"

alias m="free -h"
alias df="df -h --exclude-type=fuse.gvfsd-fuse"
alias mp='mpstat -P ALL'
#alias dfs="df -h | grep shm"
alias U='nautilus /'

alias dr="sudo systemctl daemon-reload"






#Usefull Command
#sudo chmod 600 /etc/netplan/01-network-manager-all.yaml
#sudo ip -s -s neigh flush all
#sudo arp-scan --interface=enp0s1 192.168.2.0/24


#sudo nmcli connection reload
#sudo nmcli connection down "Tenda_C7A290"  # Replace with your connection name if different
#sudo nmcli connection up "Tenda_C7A290"



#sudo dhclient -v -r eth0
#sudo dhclient -v eth0
#lxc exec Ubuntu -- bash -c 'sudo ip addr add 10.227.253.10/24 dev eth0'
alias pst="pstree -p"




function T() {
    temp=$(cat /sys/class/thermal/thermal_zone0/temp)
    temp_c=$(echo "scale=2; $temp / 1000" | bc)
    echo "Battery Temperature: $temp_c°C" | lolcat
}
alias T='T'



#sudo env PATH=$PATH /home/dev/notify.sh






alias drop1='sudo sh -c '\''echo 1 > /proc/sys/vm/drop_caches && echo "$(date): Cache level 2 dropped successfully" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\''; \
sudo sh -c '\''echo 2 > /proc/sys/vm/drop_caches && echo "$(date): Cache level 1 dropped successfully" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\''; \
sudo sh -c '\''echo 3 > /proc/sys/vm/drop_caches && echo "$(date): Cache level 3 dropped successfully" >> /var/log/cleaner/Caches-Cleaner/drop_caches_1.log'\'''



alias drop2='sudo sh -c '\''sync; echo 1 > /proc/sys/vm/drop_caches && echo "$(date): Cache level 1 dropped with sync successfully" >> /var/log/cleaner/Caches-Cleaner/drop_caches_2.log'\''; \
sudo sh -c '\''sync; echo 2 > /proc/sys/vm/drop_caches && echo "$(date): Cache level 3 dropped with sync successfully" >> /var/log/cleaner/Caches-Cleaner/drop_caches_2.log'\''; \
sudo sh -c '\''sync; echo 3 > /proc/sys/vm/drop_caches && echo "$(date): Cache level 2 dropped with sync successfully" >> /var/log/cleaner/Caches-Cleaner/drop_caches_2.log'\'''



#--prompt='●➜ '"



export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS --color=fg:#8ebf96,bg:#121212,hl:#b0b0b0 --color=fg+:#d0d0d0,bg+:#262626,hl+:#b32727 --color=info:#eb7d00,prompt:#2AA198,pointer:#2aa198 --color=marker:#9e6c2b,spinner:#ffd900,header:#b58900 --prompt='●➜ '"


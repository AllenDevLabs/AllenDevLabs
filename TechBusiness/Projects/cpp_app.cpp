#include <iostream>
#include <string>
#include <vector>

class InventoryItem {
public:
    InventoryItem(std::string name, int qty) : name(name), qty(qty) {}
    void show() const {
        std::cout << name << " x" << qty << "\n";
    }
private:
    std::string name;
    int qty;
};

int main() {
    std::vector<InventoryItem> items;
    items.push_back(InventoryItem("Router", 3));
    items.push_back(InventoryItem("Monitor", 2));
    std::cout << "[C++] Inventory tracker\n";
    for (std::vector<InventoryItem>::const_iterator it = items.begin(); it != items.end(); ++it) {
        it->show();
    }
    return 0;
}
